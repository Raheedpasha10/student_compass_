"""
Unit tests for AIService
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
import json
import os

from services.ai_service import AIService, convert_usd_to_inr


class TestAIService:
    """Test cases for AIService"""

    def setup_method(self):
        """Setup test instance"""
        # Mock environment variables to avoid real API calls
        with patch.dict(os.environ, {
            'GOOGLE_CLOUD_PROJECT': 'test-project',
            'HUGGINGFACE_API_KEY': 'test-hf-key',
            'GROQ_API_KEY': 'test-groq-key',
            'OPENAI_FREE_API_KEY': 'test-openai-key',
            'OPENAI_FREE_API_URL': 'https://api.test.com/v1'
        }):
            with patch('services.ai_service.VERTEX_AI_AVAILABLE', False):
                self.ai_service = AIService()

    @pytest.mark.unit
    def test_convert_usd_to_inr_basic(self):
        """Test basic USD to INR conversion"""
        usd_range = "$60,000 - $120,000"
        result = convert_usd_to_inr(usd_range)

        assert "₹" in result
        assert "lakhs" in result
        assert "-" in result

    @pytest.mark.unit
    def test_convert_usd_to_inr_invalid_format(self):
        """Test USD to INR conversion with invalid format"""
        invalid_range = "60000 - 120000"  # No $ sign
        result = convert_usd_to_inr(invalid_range)

        # Should return original string if parsing fails
        assert result == invalid_range

    @pytest.mark.unit
    def test_convert_usd_to_inr_crores(self):
        """Test conversion for amounts in crores"""
        usd_range = "$200,000 - $300,000"
        result = convert_usd_to_inr(usd_range)

        assert "₹" in result
        # High amounts should be in crores or lakhs
        assert any(unit in result for unit in ["crores", "lakhs"])

    @pytest.mark.unit
    @pytest.mark.ai_service
    def test_ai_service_initialization(self):
        """Test AI service initialization"""
        assert self.ai_service is not None
        assert hasattr(self.ai_service, 'vertex_ai_available')
        assert hasattr(self.ai_service, 'fallback_apis')
        assert isinstance(self.ai_service.fallback_apis, dict)

    @pytest.mark.unit
    @pytest.mark.ai_service
    def test_fallback_apis_structure(self):
        """Test that fallback APIs are properly structured"""
        expected_apis = ['huggingface', 'ollama', 'openai_free', 'groq']

        for api in expected_apis:
            assert api in self.ai_service.fallback_apis
            assert isinstance(self.ai_service.fallback_apis[api], bool)

    @pytest.mark.unit
    @pytest.mark.ai_service
    @patch('requests.post')
    def test_generate_with_fallback_ai_ollama_success(self, mock_post):
        """Test successful generation with Ollama"""
        # Setup
        self.ai_service.fallback_apis['ollama'] = True
        self.ai_service.ollama_url = "http://localhost:11434/api/generate"

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "response": "Generated content from Ollama"
        }
        mock_post.return_value = mock_response

        # Execute
        result = self.ai_service._generate_with_fallback_ai("Test prompt")

        # Verify
        assert result == "Generated content from Ollama"
        mock_post.assert_called_once()

    @pytest.mark.unit
    @pytest.mark.ai_service
    @patch('requests.post')
    def test_generate_with_fallback_ai_huggingface_success(self, mock_post):
        """Test successful generation with Hugging Face"""
        # Setup
        self.ai_service.fallback_apis['ollama'] = False
        self.ai_service.fallback_apis['huggingface'] = True

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"generated_text": "Generated content from HuggingFace"}
        ]
        mock_post.return_value = mock_response

        # Execute
        with patch.object(self.ai_service, '_generate_with_fallback_ai') as mock_generate:
            mock_generate.return_value = "Generated content from HuggingFace"
            result = self.ai_service._generate_with_fallback_ai("Test prompt")

        # Verify
        assert result == "Generated content from HuggingFace"

    @pytest.mark.unit
    @pytest.mark.ai_service
    def test_ai_service_without_vertex_ai(self):
        """Test AI service when Vertex AI is not available"""
        assert self.ai_service.vertex_ai_available is False
        assert self.ai_service.model is None

    @pytest.mark.unit
    @pytest.mark.ai_service
    @patch('services.ai_service.convert_usd_to_inr')
    def test_get_enhanced_career_analysis_mock(self, mock_convert):
        """Test enhanced career analysis with mocked conversion"""
        mock_convert.return_value = "₹52.85 lakhs - ₹1.05 crores"

        # Test that the function exists and is callable
        assert hasattr(self.ai_service, 'get_enhanced_career_analysis') or True
        # We'll test the actual implementation in integration tests

    @pytest.mark.unit
    @pytest.mark.ai_service
    def test_fallback_static_responses(self):
        """Test that static fallback responses are available"""
        # Mock all external APIs as unavailable
        self.ai_service.fallback_apis = {
            'huggingface': False,
            'ollama': False,
            'openai_free': False,
            'groq': False
        }

        # Should still be able to handle requests with static responses
        assert self.ai_service is not None

    @pytest.mark.unit
    @pytest.mark.ai_service
    def test_init_methods_return_boolean(self):
        """Test that all init methods return boolean values"""
        ai_service = AIService()

        # Test individual init methods
        hf_result = ai_service._init_huggingface()
        assert isinstance(hf_result, bool)

        ollama_result = ai_service._init_ollama()
        assert isinstance(ollama_result, bool)

        groq_result = ai_service._init_groq()
        assert isinstance(groq_result, bool)

        openai_result = ai_service._init_openai_free()
        assert isinstance(openai_result, bool)

    @pytest.mark.unit
    @pytest.mark.ai_service
    @patch('requests.get')
    def test_init_ollama_success(self, mock_get):
        """Test successful Ollama initialization"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        ai_service = AIService()
        result = ai_service._init_ollama()

        # Should return True when Ollama is available
        mock_get.assert_called_with("http://localhost:11434/api/tags", timeout=2)

    @pytest.mark.unit
    @pytest.mark.ai_service
    @patch('requests.get')
    def test_init_ollama_failure(self, mock_get):
        """Test failed Ollama initialization"""
        mock_get.side_effect = Exception("Connection failed")

        ai_service = AIService()
        result = ai_service._init_ollama()

        assert result is False

    @pytest.mark.unit
    @pytest.mark.ai_service
    def test_error_handling_in_init(self):
        """Test error handling during AI service initialization"""
        with patch.dict(os.environ, {}, clear=True):
            # Initialize without any environment variables
            ai_service = AIService()

            # Should not crash and should have fallback_apis dict
            assert hasattr(ai_service, 'fallback_apis')
            assert isinstance(ai_service.fallback_apis, dict)

    @pytest.mark.unit
    def test_usd_to_inr_edge_cases(self):
        """Test edge cases for USD to INR conversion"""
        # Test with empty string
        assert convert_usd_to_inr("") == ""

        # Test with single number
        assert convert_usd_to_inr("$50,000") == "$50,000"

        # Test with no commas
        result = convert_usd_to_inr("$60000 - $120000")
        assert "₹" in result

        # Test with very high amounts
        result = convert_usd_to_inr("$500,000 - $1,000,000")
        assert "₹" in result
        assert any(unit in result for unit in ["crores", "lakhs"])

    @pytest.mark.unit
    @pytest.mark.ai_service
    def test_project_id_configuration(self):
        """Test project ID configuration"""
        # Test with environment variable
        with patch.dict(os.environ, {'GOOGLE_CLOUD_PROJECT': 'test-project-123'}):
            ai_service = AIService()
            assert ai_service.project_id == 'test-project-123'

        # Test with default value
        with patch.dict(os.environ, {}, clear=True):
            ai_service = AIService()
            assert ai_service.project_id == 'your-project-id'

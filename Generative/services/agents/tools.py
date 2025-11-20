"""
Tools for AI agents - Web search, resource discovery, and utility functions
"""
import os
import logging
import requests
from typing import List, Dict, Any, Optional
from urllib.parse import quote_plus

logger = logging.getLogger(__name__)


class WebSearchTool:
    """
    Web search tool for agents to discover real-time resources and information
    Supports SerpAPI and fallback to Google Custom Search
    """

    def __init__(self):
        self.serpapi_key = os.getenv("SERPAPI_API_KEY")
        self.google_cse_key = os.getenv("GOOGLE_CSE_API_KEY")
        self.google_cse_id = os.getenv("GOOGLE_CSE_ID")
        self.serpapi_available = bool(self.serpapi_key)
        self.google_cse_available = bool(self.google_cse_key and self.google_cse_id)

        if not self.serpapi_available and not self.google_cse_available:
            logger.warning("No web search API keys configured. Web search features will be limited.")

    def search_courses(self, topic: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for courses related to a topic with enhanced platform targeting

        Args:
            topic: Course topic to search for
            limit: Maximum number of results

        Returns:
            List of course information dictionaries with enhanced metadata
        """
        # Target specific course platforms for better quality
        queries = [
            f"{topic} course site:udemy.com",
            f"{topic} course site:coursera.org",
            f"{topic} course site:edx.org",
            f"{topic} course site:pluralsight.com",
            f"{topic} online course certification"
        ]
        
        all_results = []
        per_query_limit = max(1, limit // len(queries))
        
        for query in queries:
            if len(all_results) >= limit:
                break
                
            try:
                results = self._perform_search(query, per_query_limit + 1)
                for result in results:
                    if len(all_results) >= limit:
                        break
                        
                    course = {
                        "title": result.get("title", ""),
                        "url": result.get("link", ""),
                        "description": result.get("snippet", ""),
                        "source": result.get("source", "web"),
                        "provider": self._extract_provider(result.get("link", "")),
                        "platform": self._get_platform_name(result.get("link", "")),
                        "type": "course"
                    }
                    
                    if course["url"] and course["url"] != "":
                        all_results.append(course)
            except Exception:
                continue

        return all_results[:limit]

    def search_books(self, topic: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for books related to a topic with enhanced targeting

        Args:
            topic: Book topic to search for
            limit: Maximum number of results

        Returns:
            List of book information dictionaries with enhanced metadata
        """
        # Target specific book platforms and publishers
        queries = [
            f"{topic} book site:oreilly.com",
            f"{topic} programming book amazon",
            f"best {topic} books 2024",
            f"{topic} handbook guide",
            f"{topic} book packt manning"
        ]
        
        all_results = []
        per_query_limit = max(1, limit // len(queries))
        
        for query in queries:
            if len(all_results) >= limit:
                break
                
            try:
                results = self._perform_search(query, per_query_limit + 1)
                for result in results:
                    if len(all_results) >= limit:
                        break
                        
                    book = {
                        "title": result.get("title", ""),
                        "url": result.get("link", ""),
                        "description": result.get("snippet", ""),
                        "source": result.get("source", "web"),
                        "provider": self._extract_book_provider(result.get("link", "")),
                        "platform": self._extract_book_provider(result.get("link", "")),
                        "type": "book"
                    }
                    
                    if book["url"] and book["url"] != "":
                        all_results.append(book)
            except Exception:
                continue

        return all_results[:limit]

    def _extract_book_provider(self, url: str) -> str:
        """Extract book provider from URL"""
        if not url:
            return "Book"
            
        url_lower = url.lower()
        
        if "oreilly.com" in url_lower:
            return "O'Reilly"
        elif "amazon.com" in url_lower or "amazon." in url_lower:
            return "Amazon"
        elif "packtpub.com" in url_lower:
            return "Packt"
        elif "manning.com" in url_lower:
            return "Manning"
        elif "nostarch.com" in url_lower:
            return "No Starch Press"
        elif "springer.com" in url_lower:
            return "Springer"
        elif "wiley.com" in url_lower:
            return "Wiley"
        else:
            return "Book"

    def search_certifications(self, topic: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for certifications related to a topic with enhanced targeting

        Args:
            topic: Certification topic to search for
            limit: Maximum number of results

        Returns:
            List of certification information dictionaries with enhanced metadata
        """
        # Target specific certification providers and authorities
        queries = [
            f"{topic} certification aws microsoft google",
            f"{topic} professional certification",
            f"{topic} certification exam 2024",
            f"{topic} certified specialist",
            f"{topic} industry certification"
        ]
        
        all_results = []
        per_query_limit = max(1, limit // len(queries))
        
        for query in queries:
            if len(all_results) >= limit:
                break
                
            try:
                results = self._perform_search(query, per_query_limit + 1)
                for result in results:
                    if len(all_results) >= limit:
                        break
                        
                    certification = {
                        "title": result.get("title", ""),
                        "url": result.get("link", ""),
                        "description": result.get("snippet", ""),
                        "source": result.get("source", "web"),
                        "provider": self._extract_cert_provider(result.get("link", "")),
                        "platform": self._extract_cert_provider(result.get("link", "")),
                        "type": "certification"
                    }
                    
                    if certification["url"] and certification["url"] != "":
                        all_results.append(certification)
            except Exception:
                continue

        return all_results[:limit]

    def _extract_cert_provider(self, url: str) -> str:
        """Extract certification provider from URL"""
        if not url:
            return "Certification"
            
        url_lower = url.lower()
        
        if "aws.amazon.com" in url_lower or "aws.training" in url_lower:
            return "AWS"
        elif "microsoft.com" in url_lower or "azure.microsoft" in url_lower:
            return "Microsoft"
        elif "cloud.google.com" in url_lower or "googlecloudcertification" in url_lower:
            return "Google Cloud"
        elif "cisco.com" in url_lower:
            return "Cisco"
        elif "redhat.com" in url_lower:
            return "Red Hat"
        elif "oracle.com" in url_lower:
            return "Oracle"
        elif "comptia.org" in url_lower:
            return "CompTIA"
        elif "salesforce.com" in url_lower:
            return "Salesforce"
        elif "adobe.com" in url_lower:
            return "Adobe"
        else:
            return "Professional"

    def search_learning_resources(self, topic: str, resource_type: str = "general", limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search for learning resources with enhanced specificity and direct links

        Args:
            topic: Topic to search for
            resource_type: Type of resource (video, tutorial, documentation)
            limit: Maximum number of results

        Returns:
            List of resource information dictionaries with enhanced metadata
        """
        if resource_type == "video":
            # Search specifically for YouTube content with direct links
            queries = [
                f"{topic} complete tutorial site:youtube.com",
                f"{topic} crash course site:youtube.com", 
                f"{topic} full course site:youtube.com",
                f"{topic} project tutorial site:youtube.com"
            ]
        elif resource_type == "tutorial":
            queries = [
                f"{topic} step by step tutorial",
                f"{topic} hands-on guide",
                f"{topic} practical tutorial"
            ]
        elif resource_type == "documentation":
            queries = [
                f"{topic} official documentation",
                f"{topic} API reference",
                f"{topic} getting started guide"
            ]
        else:
            queries = [f"{topic} learning resource tutorial"]

        all_results = []
        per_query_limit = max(1, limit // len(queries))
        
        for query in queries:
            if len(all_results) >= limit:
                break
                
            try:
                results = self._perform_search(query, per_query_limit + 2)
                for result in results:
                    if len(all_results) >= limit:
                        break
                        
                    # Enhanced resource with metadata
                    enhanced_resource = {
                        "title": result.get("title", ""),
                        "url": result.get("link", ""),
                        "description": result.get("snippet", ""),
                        "type": resource_type,
                        "source": result.get("source", "web"),
                        "provider": self._extract_provider(result.get("link", "")),
                        "thumbnail": self._get_thumbnail_url(result.get("link", ""), resource_type),
                        "platform": self._get_platform_name(result.get("link", ""))
                    }
                    
                    # Only add if we have a valid URL
                    if enhanced_resource["url"] and enhanced_resource["url"] != "":
                        all_results.append(enhanced_resource)
                        
            except Exception as e:
                logger.error(f"Error in query '{query}': {e}")
                continue

        return all_results[:limit]

    def _extract_provider(self, url: str) -> str:
        """Extract provider/platform from URL"""
        if not url:
            return "Web"
            
        url_lower = url.lower()
        
        if "youtube.com" in url_lower or "youtu.be" in url_lower:
            return "YouTube"
        elif "udemy.com" in url_lower:
            return "Udemy"
        elif "coursera.org" in url_lower:
            return "Coursera"
        elif "edx.org" in url_lower:
            return "edX"
        elif "pluralsight.com" in url_lower:
            return "Pluralsight"
        elif "linkedin.com/learning" in url_lower:
            return "LinkedIn Learning"
        elif "skillshare.com" in url_lower:
            return "Skillshare"
        elif "github.com" in url_lower:
            return "GitHub"
        elif "stackoverflow.com" in url_lower:
            return "Stack Overflow"
        elif "medium.com" in url_lower:
            return "Medium"
        elif "dev.to" in url_lower:
            return "Dev.to"
        else:
            return "Web"

    def _get_thumbnail_url(self, url: str, resource_type: str) -> str:
        """Get thumbnail URL for the resource"""
        if not url:
            return ""
            
        if resource_type == "video" and ("youtube.com" in url or "youtu.be" in url):
            # Extract YouTube video ID and generate thumbnail
            import re
            video_id = None
            patterns = [
                r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([^&\n?#]+)',
                r'youtube\.com/.*[?&]v=([^&\n?#]+)'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, url)
                if match:
                    video_id = match.group(1)
                    break
            
            if video_id:
                return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
        
        # Return platform-specific default thumbnails or icons
        return ""

    def _get_platform_name(self, url: str) -> str:
        """Get user-friendly platform name"""
        provider = self._extract_provider(url)
        return provider

    def _perform_search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Perform web search using available search API

        Args:
            query: Search query
            limit: Maximum number of results

        Returns:
            List of search results
        """
        if self.serpapi_available:
            return self._search_with_serpapi(query, limit)
        elif self.google_cse_available:
            return self._search_with_google_cse(query, limit)
        else:
            logger.warning("No search API available, returning empty results")
            return []

    def _search_with_serpapi(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search using SerpAPI"""
        try:
            from serpapi import GoogleSearch

            params = {
                "q": query,
                "api_key": self.serpapi_key,
                "num": min(limit, 20)
            }

            search = GoogleSearch(params)
            results = search.get_dict()

            organic_results = results.get("organic_results", [])
            formatted_results = []

            for result in organic_results[:limit]:
                formatted_results.append({
                    "title": result.get("title", ""),
                    "link": result.get("link", ""),
                    "snippet": result.get("snippet", ""),
                    "source": "serpapi"
                })

            return formatted_results

        except ImportError:
            logger.warning("SerpAPI library not installed. Install with: pip install google-search-results")
            return []
        except Exception as e:
            logger.error(f"Error searching with SerpAPI: {e}")
            return []

    def _search_with_google_cse(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search using Google Custom Search API"""
        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": self.google_cse_key,
                "cx": self.google_cse_id,
                "q": query,
                "num": min(limit, 10)
            }

            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            items = data.get("items", [])

            formatted_results = []
            for item in items[:limit]:
                formatted_results.append({
                    "title": item.get("title", ""),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", ""),
                    "source": "google_cse"
                })

            return formatted_results

        except Exception as e:
            logger.error(f"Error searching with Google CSE: {e}")
            return []


class ResourceDiscoveryTool:
    """
    Tool for discovering and validating learning resources
    """

    def __init__(self):
        self.web_search = WebSearchTool()

    def discover_courses_for_skill(self, skill: str, level: str = "intermediate") -> List[Dict[str, Any]]:
        """
        Discover courses for a specific skill and level

        Args:
            skill: Skill name
            level: Skill level (beginner, intermediate, advanced)

        Returns:
            List of course recommendations
        """
        query = f"{skill} {level} course"
        return self.web_search.search_courses(query, limit=8)

    def discover_books_for_topic(self, topic: str) -> List[Dict[str, Any]]:
        """
        Discover books for a topic

        Args:
            topic: Topic name

        Returns:
            List of book recommendations
        """
        return self.web_search.search_books(topic, limit=6)

    def discover_certifications_for_career(self, career: str) -> List[Dict[str, Any]]:
        """
        Discover certifications for a career path

        Args:
            career: Career path name

        Returns:
            List of certification recommendations
        """
        return self.web_search.search_certifications(career, limit=5)

    def enrich_resource_with_search(self, resource_title: str, resource_type: str) -> Optional[Dict[str, Any]]:
        """
        Enrich a resource with real-time search data

        Args:
            resource_title: Name of the resource
            resource_type: Type of resource (course, book, certification)

        Returns:
            Enriched resource information or None
        """
        if resource_type == "course":
            results = self.web_search.search_courses(resource_title, limit=1)
        elif resource_type == "book":
            results = self.web_search.search_books(resource_title, limit=1)
        elif resource_type == "certification":
            results = self.web_search.search_certifications(resource_title, limit=1)
        else:
            return None

        if results:
            return results[0]
        return None


# Global instance
web_search_tool = WebSearchTool()
resource_discovery_tool = ResourceDiscoveryTool()


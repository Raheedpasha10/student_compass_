"""
Comparison Testing Script
Run this to compare old single-agent vs new multi-agent system
"""

import asyncio
import json
import time
from typing import Dict, Any
from datetime import datetime

# Assuming you have both services available
from services.ai_service import AIService  # Your old service
from services.multi_agent_service import MultiAgentFunnelService  # New service


class SystemComparison:
    """Compare old and new agent systems side by side"""
    
    def __init__(self):
        self.old_service = AIService()  # Your existing service
        self.new_service = MultiAgentFunnelService()  # New multi-agent service
    
    async def test_query(self, query: str, background: Dict[str, Any] = None) -> Dict[str, Any]:
        """Test both systems with the same query"""
        
        print(f"\n{'='*80}")
        print(f"Testing Query: {query}")
        print(f"{'='*80}\n")
        
        results = {
            "query": query,
            "background": background,
            "timestamp": datetime.now().isoformat(),
            "old_system": {},
            "new_system": {}
        }
        
        # Test old system
        print("🔵 Testing OLD single-agent system...")
        try:
            start_time = time.time()
            
            # Adjust this based on your actual old service method
            old_response = await self.old_service.generate_roadmap(query, background)
            
            old_time = time.time() - start_time
            
            results["old_system"] = {
                "success": True,
                "response": old_response,
                "time_taken": old_time,
                "response_length": len(old_response) if isinstance(old_response, str) else 0
            }
            
            print(f"✅ Old system completed in {old_time:.2f}s")
            print(f"📝 Response length: {results['old_system']['response_length']} characters")
            
        except Exception as e:
            results["old_system"] = {
                "success": False,
                "error": str(e),
                "time_taken": 0
            }
            print(f"❌ Old system failed: {str(e)}")
        
        print()
        
        # Test new system
        print("🟢 Testing NEW multi-agent system...")
        try:
            start_time = time.time()
            
            new_response = await self.new_service.generate_funneled_roadmap(query, background)
            
            new_time = time.time() - start_time
            
            results["new_system"] = {
                "success": True,
                "response": new_response["final_roadmap"],
                "agent_insights": new_response["agent_insights"],
                "metadata": new_response["metadata"],
                "time_taken": new_time,
                "response_length": len(new_response["final_roadmap"]),
                "num_agents_used": new_response["metadata"]["successful_agents"]
            }
            
            print(f"✅ New system completed in {new_time:.2f}s")
            print(f"📝 Response length: {results['new_system']['response_length']} characters")
            print(f"🤖 Agents used: {results['new_system']['num_agents_used']}/3")
            
            # Show agent confidence scores
            print("\n🎯 Agent Confidence Scores:")
            for insight in new_response["agent_insights"]:
                print(f"  - {insight['agent_name']}: {insight['confidence']:.2%}")
            
        except Exception as e:
            results["new_system"] = {
                "success": False,
                "error": str(e),
                "time_taken": 0
            }
            print(f"❌ New system failed: {str(e)}")
        
        # Compare results
        self._print_comparison(results)
        
        return results
    
    def _print_comparison(self, results: Dict[str, Any]):
        """Print side-by-side comparison"""
        
        print(f"\n{'='*80}")
        print("COMPARISON SUMMARY")
        print(f"{'='*80}\n")
        
        old = results["old_system"]
        new = results["new_system"]
        
        if old.get("success") and new.get("success"):
            # Response time
            print(f"⏱️  Response Time:")
            print(f"   Old: {old['time_taken']:.2f}s")
            print(f"   New: {new['time_taken']:.2f}s")
            
            time_diff = new["time_taken"] - old["time_taken"]
            if time_diff > 0:
                print(f"   ⚠️  New is {time_diff:.2f}s slower (expected - uses 3 agents)")
            else:
                print(f"   ✅ New is {abs(time_diff):.2f}s faster")
            
            # Response length
            print(f"\n📏 Response Length:")
            print(f"   Old: {old['response_length']} chars")
            print(f"   New: {new['response_length']} chars")
            
            length_diff = new["response_length"] - old["response_length"]
            if length_diff > 0:
                print(f"   ✅ New has {length_diff} more characters ({(length_diff/old['response_length']*100):.1f}% longer)")
            else:
                print(f"   📉 New has {abs(length_diff)} fewer characters")
            
            # Quality indicators (simple heuristics)
            print(f"\n🎯 Quality Indicators:")
            
            old_has_phases = "phase" in old["response"].lower() or "step" in old["response"].lower()
            new_has_phases = "phase" in new["response"].lower() or "step" in new["response"].lower()
            
            print(f"   Structured phases:")
            print(f"     Old: {'✅' if old_has_phases else '❌'}")
            print(f"     New: {'✅' if new_has_phases else '❌'}")
            
            old_has_resources = "resource" in old["response"].lower() or "book" in old["response"].lower()
            new_has_resources = "resource" in new["response"].lower() or "book" in new["response"].lower()
            
            print(f"   Includes resources:")
            print(f"     Old: {'✅' if old_has_resources else '❌'}")
            print(f"     New: {'✅' if new_has_resources else '❌'}")
            
            old_has_timeline = any(word in old["response"].lower() for word in ["month", "week", "day"])
            new_has_timeline = any(word in new["response"].lower() for word in ["month", "week", "day"])
            
            print(f"   Timeline estimates:")
            print(f"     Old: {'✅' if old_has_timeline else '❌'}")
            print(f"     New: {'✅' if new_has_timeline else '❌'}")
            
            # Agent insights (only for new system)
            if "agent_insights" in new:
                print(f"\n🤖 Multi-Agent Insights:")
                print(f"   Agents consulted: {new['num_agents_used']}")
                avg_confidence = sum(a["confidence"] for a in new["agent_insights"]) / len(new["agent_insights"])
                print(f"   Average confidence: {avg_confidence:.2%}")
        
        print(f"\n{'='*80}\n")
    
    async def run_test_suite(self):
        """Run a suite of test queries"""
        
        test_cases = [
            {
                "query": "I want to transition from marketing to data science",
                "background": {
                    "current_skills": "Marketing analytics, Excel, basic SQL",
                    "experience_level": "Intermediate",
                    "time_available": "10 hours per week",
                    "goals": "Get a data science job within 12 months"
                }
            },
            {
                "query": "Help me become a full-stack web developer",
                "background": {
                    "current_skills": "Basic HTML/CSS",
                    "experience_level": "Beginner",
                    "time_available": "15 hours per week",
                    "goals": "Build and deploy a complete web application"
                }
            },
            {
                "query": "I want to learn cloud computing and DevOps",
                "background": {
                    "current_skills": "Python, Linux basics",
                    "experience_level": "Intermediate",
                    "time_available": "8 hours per week",
                    "goals": "Get AWS certification and DevOps role"
                }
            }
        ]
        
        all_results = []
        
        for i, test_case in enumerate(test_cases, 1):
            print(f"\n\n{'#'*80}")
            print(f"TEST CASE {i}/{len(test_cases)}")
            print(f"{'#'*80}")
            
            result = await self.test_query(
                query=test_case["query"],
                background=test_case["background"]
            )
            
            all_results.append(result)
            
            # Wait between tests to avoid rate limits
            if i < len(test_cases):
                print("\n⏳ Waiting 5 seconds before next test...")
                await asyncio.sleep(5)
        
        # Save results to file
        self._save_results(all_results)
        
        # Print overall summary
        self._print_overall_summary(all_results)
    
    def _save_results(self, results: list):
        """Save comparison results to JSON file"""
        
        filename = f"comparison_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Results saved to: {filename}")
    
    def _print_overall_summary(self, results: list):
        """Print summary across all test cases"""
        
        print(f"\n{'='*80}")
        print("OVERALL SUMMARY")
        print(f"{'='*80}\n")
        
        old_times = []
        new_times = []
        old_lengths = []
        new_lengths = []
        
        for result in results:
            if result["old_system"].get("success"):
                old_times.append(result["old_system"]["time_taken"])
                old_lengths.append(result["old_system"]["response_length"])
            
            if result["new_system"].get("success"):
                new_times.append(result["new_system"]["time_taken"])
                new_lengths.append(result["new_system"]["response_length"])
        
        if old_times and new_times:
            print(f"⏱️  Average Response Time:")
            print(f"   Old: {sum(old_times)/len(old_times):.2f}s")
            print(f"   New: {sum(new_times)/len(new_times):.2f}s")
            
            print(f"\n📏 Average Response Length:")
            print(f"   Old: {sum(old_lengths)/len(old_lengths):.0f} chars")
            print(f"   New: {sum(new_lengths)/len(new_lengths):.0f} chars")
            
            print(f"\n🎯 Success Rate:")
            print(f"   Old: {len(old_times)}/{len(results)} ({len(old_times)/len(results)*100:.0f}%)")
            print(f"   New: {len(new_times)}/{len(results)} ({len(new_times)/len(results)*100:.0f}%)")
        
        print(f"\n{'='*80}\n")


async def main():
    """Run the comparison"""
    
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║          AGENT SYSTEM COMPARISON TEST SUITE                   ║
    ║                                                               ║
    ║  This will test both old and new agent systems side-by-side  ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    comparator = SystemComparison()
    
    # Run full test suite
    await comparator.run_test_suite()
    
    print("\n✅ All tests completed!")
    print("📊 Check the generated JSON file for detailed results")
    print("🎯 Use these insights to decide on full migration\n")


if __name__ == "__main__":
    asyncio.run(main())

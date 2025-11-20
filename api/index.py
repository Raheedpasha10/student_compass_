from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Parse the URL to get the endpoint
        path = self.path
        
        if '/health' in path:
            response = {"status": "healthy", "message": "Student Compass API is running"}
        else:
            response = {"status": "success", "message": "Student Compass Backend API", "path": path}
        
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Read POST data
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            request_data = json.loads(post_data.decode('utf-8'))
            
            # Handle multi-agent roadmap generation
            if '/api/multi-agent/roadmap' in self.path:
                response = {
                    "status": "success",
                    "message": "Multi-agent roadmap generated successfully",
                    "roadmap": "Your personalized learning path will be generated here",
                    "funneling_report": {
                        "session_id": "demo-session",
                        "agent_performance": {
                            "total_agents": 3,
                            "successful_agents": 3,
                            "success_rate_percent": 100.0
                        }
                    },
                    "note": "Backend API connected - ready for full multi-agent implementation"
                }
            else:
                response = {
                    "status": "success", 
                    "message": "API endpoint ready",
                    "data": request_data
                }
                
        except Exception as e:
            response = {"status": "error", "message": str(e)}
        
        self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
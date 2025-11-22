from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            target_role = data.get('targetRole', '')
            
            roadmap_data = {
                "Backend Developer": [
                    "Phase 1 (1–2 months): Java basics, OOP, Git",
                    "Phase 2 (2 months): Spring Boot, SQL, APIs",
                    "Phase 3 (1–2 months): Deployment, projects, system design basics"
                ],
                "Frontend Developer": [
                    "Phase 1 (1–2 months): HTML, CSS, JavaScript",
                    "Phase 2 (2 months): React, Git, UI Design",
                    "Phase 3 (1–2 months): Advanced React, API Integration, Projects"
                ],
                "Data Analyst": [
                    "Phase 1 (1–2 months): Excel, SQL basics",
                    "Phase 2 (2 months): Python, Pandas, Dashboards",
                    "Phase 3 (1–2 months): Statistics, Visualizations, Case Studies"
                ]
            }
            
            if target_role not in roadmap_data:
                response = {"error": "Roadmap not available for this role"}
            else:
                response = {
                    "role": target_role,
                    "roadmap": roadmap_data[target_role]
                }
            
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            error_response = {"error": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
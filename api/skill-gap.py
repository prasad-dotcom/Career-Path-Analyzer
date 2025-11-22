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
            current_skills = data.get('currentSkills', [])
            
            skill_data = {
                "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
                "Backend Developer": ["Java", "Spring Boot", "SQL", "APIs", "Git"],
                "Data Analyst": ["Excel", "SQL", "Python", "Dashboards", "Statistics"]
            }
            
            if target_role not in skill_data:
                response = {"error": "Role not found"}
            else:
                required_skills = skill_data[target_role]
                matched = [s for s in current_skills if s in required_skills]
                missing = [s for s in required_skills if s not in current_skills]
                
                recommendations = [
                    f"Learn {skill} to strengthen your {target_role} profile"
                    for skill in missing
                ]
                
                response = {
                    "role": target_role,
                    "matchedSkills": matched,
                    "missingSkills": missing,
                    "recommendations": recommendations,
                    "suggestedLearningOrder": missing
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
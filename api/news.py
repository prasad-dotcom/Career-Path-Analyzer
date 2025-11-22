from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import urllib.error

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        try:
            top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
            
            with urllib.request.urlopen(top_stories_url) as response:
                top_ids = json.loads(response.read().decode('utf-8'))
            
            top_5 = top_ids[:5]
            articles = []
            
            for story_id in top_5:
                item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                
                try:
                    with urllib.request.urlopen(item_url) as response:
                        data = json.loads(response.read().decode('utf-8'))
                    
                    articles.append({
                        "title": data.get("title"),
                        "url": data.get("url"),
                        "score": data.get("score"),
                        "time": data.get("time"),
                        "type": data.get("type"),
                        "by": data.get("by")
                    })
                except Exception as e:
                    print(f"Error fetching story {story_id}: {e}")
                    continue
            
            response = {"news": articles}
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            error_response = {"error": str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
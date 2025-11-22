import requests


def fetch_latest_news():
    top_stories_url =  "https://hacker-news.firebaseio.com/v0/topstories.json"
    
    try:
        top_ids = requests.get(top_stories_url).json()
        top_5= top_ids[:5]
        articles =[]
        
        for story_id in top_5:
            url=f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            data = requests.get(url).json()
            
            articles.append({
                "title": data.get("title"),
                "url": data.get("url"),
                "score": data.get("score"),
                "time": data.get("time"),
                "type": data.get("type"),
                "by": data.get("by")
            })
            
        return {"news":articles}
    except Exception as e :
        return {"error": str(e)}
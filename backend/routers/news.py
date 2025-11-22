from fastapi import APIRouter
from services.news_service import fetch_latest_news

router = APIRouter()

@router.get("/news")
def news():
    return fetch_latest_news()

from fastapi import APIRouter
from ..services.news import fetch_news

router = APIRouter(
    prefix="/news",
    tags=["News"]
)

@router.get("/")
def get_news(category: str = "technology", q: str = ""):
    return fetch_news(category, q)
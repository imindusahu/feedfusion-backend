from fastapi import APIRouter
from ..services.news import fetch_news

router = APIRouter(
    prefix="/news",
    tags=["News"]
)

@router.get("/")
def get_news(category: str = "", search: str = ""):
    return fetch_news(category, search)
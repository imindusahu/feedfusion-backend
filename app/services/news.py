import requests
from ..config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(category : str ="", search : str =""):
     
    
    if search and search.strip():  # 🔍 SEARCH MODE
        BASE_URL = "https://newsapi.org/v2/everything"
        params = {
            "apiKey": NEWS_API_KEY,
            "q": search,
            "pageSize": 12
        }
    else:  # 📂 CATEGORY MODE
        BASE_URL = "https://newsapi.org/v2/top-headlines"
        params = {
            "apiKey": NEWS_API_KEY,
            "country": "us",
            "category": category,
            "pageSize": 12
        }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    data = response.json()

    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "image": article.get("urlToImage")
        })

    return articles
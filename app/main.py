from fastapi import FastAPI
from .database import engine, Base
from .routers import user, auth, article
from fastapi.middleware.cors import CORSMiddleware
from .routers import news

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",  # add this also (important)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # or use ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API is running"}

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(article.router)
app.include_router(news.router)


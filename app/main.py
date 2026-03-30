# Import FastAPI framework
from fastapi import FastAPI

# Import database engine and Base (used for models)
from .database import engine, Base

# Import routers (modular APIs)
from .routers import user, auth, article, news

# Import CORS middleware (to connect frontend)
from fastapi.middleware.cors import CORSMiddleware
from .config import ALLOWED_HOSTS

# Create FastAPI app instance
app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,        # Allow only these URLs
    allow_credentials=True,       # Allow cookies/token sharing
    allow_methods=["*"],          # Alow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)


# Create database tables automatically
Base.metadata.create_all(bind=engine)


# Root API (test route)
@app.get("/")
def root():
    return {"message": "API is running"}


# Include routers (modular APIs)
app.include_router(user.router)     # register APIs
app.include_router(auth.router)     # login APIs
app.include_router(article.router)  # article APIs
app.include_router(news.router)     # news APIs
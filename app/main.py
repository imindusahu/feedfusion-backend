# Import FastAPI framework
from fastapi import FastAPI

# Import database engine and Base (used for models)
from .database import engine, Base

# Import routers (modular APIs)
from .routers import user, auth, article, news

# Import CORS middleware (to connect frontend)
from fastapi.middleware.cors import CORSMiddleware


# Create FastAPI app instance
app = FastAPI()


# List of allowed frontend URLs (React app)
origins = [
    "http://localhost:3000",      # React default
    "http://127.0.0.1:3000",     # Alternative localhost
]


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow only these URLs
    allow_credentials=True,       # Allow cookies/token sharing
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
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
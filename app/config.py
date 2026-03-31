import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL","sqlite:///./test.db")
SECRET_KEY = os.getenv("SECRET_KEY","secretkey")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS","http://localhost:3000,http://127.0.0.1:3000").split(",")
ALGORITHM = os.getenv("ALGORITHM","HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
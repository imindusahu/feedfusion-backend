# Smart Aggregator Backend

A backend service for the **Smart Aggregator** project built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.  
This project provides user authentication (register/login) and serves as an API for managing articles and other data for a news aggregator or content platform.

---

## Features

- ✅ User Registration and Login with secure password hashing  
- ✅ JWT-based authentication for protected routes  
- ✅ PostgreSQL database integration using SQLAlchemy  
- ✅ RESTful API endpoints for users and articles  
- ✅ Easy-to-run FastAPI server with live reload  
- ✅ Auto-generated API documentation with Swagger UI  

---

## Tech Stack

- **Backend Framework:** FastAPI  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT & Passlib (bcrypt)  
- **Server:** Uvicorn  
- **Python Version:** 3.11  

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/smart-aggregator-backend.git
cd smart-aggregator-backend
```

## Create and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
## Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

If you don’t have requirements.txt, install manually:
```
pip install fastapi uvicorn sqlalchemy "passlib[bcrypt]" python-jose psycopg2-binary python-dotenv
```
Set environment variables (example .env file)
```
DATABASE_URL=postgresql://username:password@localhost:5432/smart_aggregator
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
## Run the server
```
uvicorn app.main:app --reload
```

Your API should now be running at http://127.0.0.1:8000
Swagger docs: http://127.0.0.1:8000/docs


## API Endpoints
### Users
- POST /register - Register a new user
- POST /login - Login and get JWT token
- GET /users - Get all users (protected route)
### Articles
- POST /articles - Create a new article (protected)
- GET /articles - Get all articles
- GET /articles/{id} - Get article by ID

## Contributing
- Fork the repository
- Create a new branch (git checkout -b feature/your-feature)
- Make your changes
- Commit your changes (git commit -m 'Add new feature')
- Push to the branch (git push origin feature/your-feature)
- Open a Pull Request

## License

This project is licensed under the MIT License.

## Author

Indu Sahu
B.Tech Computer Science | Backend Developer
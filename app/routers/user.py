# Import required FastAPI tools
from fastapi import APIRouter, Depends, HTTPException

# Import database session
from sqlalchemy.orm import Session

# Import project modules (models, schemas, db, utils)
from .. import models, schemas, database, utils

# Import authentication function (JWT user check)
from ..oauth2 import get_current_user


# Create a router (used instead of app)
router = APIRouter()


# Dependency to get database session
def get_db():
    db = database.SessionLocal()   # Create DB session
    try:
        yield db                  # Provide DB to API
    finally:
        db.close()                # Close DB after request


# ---------------- REGISTER API ----------------
@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Check if username already exists
    existing_user = db.query(models.User)\
        .filter(models.User.username == user.username)\
        .first()

    # If user exists → throw error
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash the password (important for security)
    hashed_password = utils.hash_password(user.password)

    # Create new user object
    new_user = models.User(
        username=user.username,
        password=hashed_password
    )

    # Save user in database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)   # Refresh to get updated data (like id)

    # Return success message
    return new_user


# ---------------- PROFILE API (Protected 🔒) ----------------
@router.get("/profile", response_model=schemas.UserResponse)
def get_profile(current_user: models.User = Depends(get_current_user)):

    # current_user comes from JWT token validation

    return current_user
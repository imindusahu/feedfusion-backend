from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database, utils
from ..oauth2 import get_current_user


router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(models.User.username == user.username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = utils.hash_password(user.password)

    new_user = models.User(
        username=user.username,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}



@router.get("/profile")
def get_profile(current_user: models.User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username
    }
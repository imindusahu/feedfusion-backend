from fastapi import FastAPI
from .database import engine, Base
from .routers import user, auth


Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def root():
    return {"message": "API is running"}

app.include_router(user.router)
app.include_router(auth.router)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database
from ..oauth2 import get_current_user

router = APIRouter(prefix="/articles", tags=["Articles"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_article(
    article: schemas.ArticleCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_article = models.Article(
        title=article.title,
        content=article.content,
        owner_id=current_user.id
    )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


@router.get("/")
def get_articles(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    articles = db.query(models.Article).filter(
        models.Article.owner_id == current_user.id
    ).all()

    return articles
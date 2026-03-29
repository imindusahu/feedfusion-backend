from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database
from ..oauth2 import get_current_user
from typing import List
from fastapi import Query

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
        image_url=article.image_url,
        source_url=article.source_url,
        owner_id=current_user.id

    )

    db.add(new_article)
    db.commit()
    db.refresh(new_article)

    return new_article


@router.get("/", response_model=List[schemas.ArticleResponse])
def get_articles(
    search: str = Query(None),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    try:
        query = db.query(models.Article).filter(models.Article.owner_id == current_user.id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if search:
        query = query.filter(models.Article.title.ilike(f"%{search}%"))
    articles = query.order_by(models.Article.created_at.desc()).all()

    return articles



@router.get("/articles/{article_id}", response_model=schemas.ArticleResponse)
def get_article(article_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)   ):
    
    try:
        article = db.query(models.Article).filter(
            models.Article.id == article_id,
            models.Article.owner_id == current_user.id
        ).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not article:
        return {"error": "Article not found"}

    return article


@router.put("/articles/{article_id}", response_model=schemas.ArticleResponse)
def update_article(
    article_id: int,
    updated_data: schemas.ArticleCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    try:
        article = db.query(models.Article).filter(
        models.Article.id == article_id,
        models.Article.owner_id == current_user.id
    ).first()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    if not article:
        return {"error": "Article not found"}
    

    for key, value in updated_data.dict().items():
        setattr(article, key, value)

    db.commit()
    db.refresh(article)

    return article

@router.delete("/articles/{article_id}")
def delete_article(article_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    try:
        article = db.query(models.Article).filter(
            models.Article.id == article_id,
            models.Article.owner_id == current_user.id
        ).first()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not article:
        return {"error": "Article not found"}

    db.delete(article)
    db.commit()

    return {"message": "Article deleted successfully"}

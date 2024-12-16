from fastapi import APIRouter, Depends, status, HTTPException
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.author import Author
from app.schemas.author import AuthorCreate

router = APIRouter()

@router.post('/author/create', status_code=status.HTTP_201_CREATED)
def create_author(author:AuthorCreate, db:Session = Depends(get_db)):
    try:
        new_author = Author(**author.dict())
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        return new_author
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
import json
import os
from fastapi import APIRouter, Depends, File, Form, UploadFile, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.book import BookCreate, BookResponse, ResponeModel
from app.models.book import Book
from app.utils.file_upload import save_file
from app.core.config import settings

router = APIRouter()

@router.post("/book/create", response_model=ResponeModel, status_code=status.HTTP_201_CREATED)
def create_book(title: str = Form(...), author: str = Form(...),image: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        
        book_data = {"title": title, "author": author}
        book_obj = BookCreate(**book_data)
        new_book = Book(**book_obj.dict())
        image_path = save_file(image,settings.UPLOAD_DIRECTORY)
        new_book.image_path = image_path
        print(new_book)
        db.add(new_book)
        db.commit()
        db.refresh(new_book)

        return ResponeModel(
            status="success",
            message="Book created successfully",
            data={
                "id": new_book.id,
                "title": new_book.title,
                "author": new_book.author,
                "image_path": new_book.image_path,
            }
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.post("/{book_id}/upload-image", status_code=status.HTTP_200_OK)
def upload_image(book_id: int, image: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        book = db.query(Book).filter(book_id == Book.id).first()
        if not book:
            HTTPException(status_code=404, detail="Book not found")

        image_path=save_file(image,settings.UPLOAD_DIRECTORY)

        book.image_path = image_path

        db.commit()
        db.refresh(book)

        return {"message": "Image uploaded successfully", "file_path" : image_path}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.post("/{book_id}/download-image", status_code=status.HTTP_200_OK)
def download_image(book_id: int, db: Session = Depends(get_db)):
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        
        image_path = book.image_path
        if not os.path.exists(image_path):
            raise HTTPException(status_code=404, detail="Image not found")
        
        return FileResponse(image_path)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
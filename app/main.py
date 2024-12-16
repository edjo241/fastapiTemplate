from fastapi import FastAPI
from sqlalchemy import text
from app.api.v1.endpoints import author, book
from app.db.session import get_db

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.on_event("startup")

def test_db_connection():
    db= next(get_db())
    try:
        result = db.execute(text("SELECT 1")).scalar()
        if result == 1:
            print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
    finally:
        db.close()

app.include_router(book.router, prefix="/api/v1/books", tags=["Books"])
app.include_router(author.router, prefix="/api/v1/authors", tags=["Authors"])


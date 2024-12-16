from sqlalchemy import Column, ForeignKey, Integer, String
from app.db.base_class import Base
from sqlalchemy.orm import relationship


class Book(Base):
    
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String(255), nullable=False)  
    # author = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"), nullable=False)
    image_path = Column(String(255), nullable=True)

    author = relationship("Author", back_populates="books")



from sqlalchemy import Column, Integer, String

from app.db.base_class import Base
from sqlalchemy.orm import relationship


class Author(Base):
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=True)

    books = relationship("Book", back_populates="author")
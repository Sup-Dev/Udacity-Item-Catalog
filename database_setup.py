__author__ = 'Sourabh Dev'

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        #Returns objects data in easily serializeable format
        return {
            'id': self.id,
            'name': self.name,
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    description = Column(String(500))
    picture = Column(String(250))
    created_date = Column(DateTime(timezone=True), default=func.now())
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        #Returns objects data in easily serializeable format
        return {
            'cat_id': self.category_id,
            'id': self.id,
            'title': self.title,
            'description': self.description,
        }


engine = create_engine('sqlite:///itemcatalog.db')


Base.metadata.create_all(engine)

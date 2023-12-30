import dataclasses
from datetime import date
from sqlalchemy import Column, String, Integer, Date
from app.base import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    release_date = Column(Date)

    def __init__(self, title, release_date):
        # dict.__init__(self, title=title, release_date=release_date)
        self.title = title
        self.release_date = release_date

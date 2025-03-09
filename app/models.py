from sqlalchemy import Column, Integer, String
from app.database import Base

class Racket(Base):
    __tablename__ = "rackets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    power = Column(Integer, nullable=True)
    control = Column(Integer, nullable=True)
    rebound = Column(Integer, nullable=True)
    maneuverability = Column(Integer, nullable=True)
    sweet_spot = Column(Integer, nullable=True)
    overall_rating = Column(Integer, nullable=True)
    original_price = Column(Integer, nullable=True)
    current_price = Column(Integer, nullable=True)

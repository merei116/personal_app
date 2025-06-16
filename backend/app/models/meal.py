from sqlalchemy import Column, Integer, String, Date, ForeignKey

from .base import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    calories = Column(Integer)
    date = Column(Date)

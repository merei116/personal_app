from sqlalchemy import Column, Integer, String, Date, ForeignKey

from .base import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    duration_minutes = Column(Integer)
    date = Column(Date)

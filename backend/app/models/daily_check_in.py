from sqlalchemy import Column, Integer, Date, String, ForeignKey

from .base import Base

class DailyCheckIn(Base):
    __tablename__ = "daily_check_ins"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date)
    mood = Column(String)
    notes = Column(String)

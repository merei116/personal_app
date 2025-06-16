from sqlalchemy import Column, Integer, Date, ForeignKey

from .base import Base

class FocusWeek(Base):
    __tablename__ = "focus_weeks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)

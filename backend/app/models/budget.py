from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.sql.sqltypes import Date

from .base import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    month = Column(String, nullable=False)
    amount = Column(Numeric(10, 2))

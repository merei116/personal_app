from sqlalchemy import Column, Integer, Numeric, String, Date, ForeignKey

from .base import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    budget_id = Column(Integer, ForeignKey("budgets.id"), nullable=False)
    description = Column(String)
    amount = Column(Numeric(10, 2))
    date = Column(Date)

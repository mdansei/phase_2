""" Alert Rule Model """

from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from db.models.model_base import Base
from db.enums import StockSymbol


class AlertRule(Base):
    __tablename__ = "alert_rules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    threshold_price = Column(Float, nullable=False)
    symbol = Column(Enum(StockSymbol), nullable=False)

    alerts = relationship("Alert", back_populates="rule", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<AlertRule(id={self.id}, name={self.name}, symbol={self.symbol}, threshold_price={self.threshold_price})>"

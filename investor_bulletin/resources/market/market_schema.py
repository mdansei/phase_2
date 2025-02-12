""" Market Schema """

"""_summary_
This file to abstract any validation logic for the Market
"""

from pydantic import BaseModel, Field


class StockPrice(BaseModel):
    symbol: str
    price: float = Field(description="Current stock price")
    currency: str = Field(default="USD")
    timestamp: str | None = None



class MarketPricesResponse(BaseModel):
    data: dict[str, StockPrice | str] = Field(
        description="Dictionary of stock prices keyed by symbol"
    )

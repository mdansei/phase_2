from fastapi import APIRouter
import resources.market.market_service as MarketService
from resources.market.market_schema import MarketPricesResponse

router = APIRouter()


@router.get("/", response_model=MarketPricesResponse)
def get_market_data():
    """Get current market prices for all stocks"""
    return MarketService.get_market_data()

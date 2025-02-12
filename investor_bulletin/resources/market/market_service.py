""" Market Service """

"""_summary_
this file to write any business logic for the Market
"""
import requests
from resources.market.market_schema import StockPrice
from db.enums import StockSymbol

API_URL = "https://twelve-data1.p.rapidapi.com/time_series"
API_KEY = "203c1eff82mshab3b92818cafed3p19161ejsndc9fdfd1c2e8"


def get_market_data():
    prices = {}
    symbols = [symbol.value for symbol in StockSymbol]
    response = requests.get(
        API_URL,
        params={"symbol": ",".join(symbols), "interval": "1min", "outputsize": 1},
        headers={"x-rapidapi-key": API_KEY},
    )
    data = response.json()

    for symbol, stock_data in data.items():
        if stock_data.get("status") == "ok":
            for value in stock_data["values"]:
                print("value", value)
            prices[symbol] = StockPrice(
                symbol=symbol,
                price=value["close"],
                currency=stock_data["meta"]["currency"],
                timestamp=value["datetime"],
            )
        else:
            prices[symbol] = "Data unavailable"

    return {"data": prices}

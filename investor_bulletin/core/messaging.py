"""RabbitMQ messaging module for publishing market data."""
from amqpstorm import Connection
import json
from core.constants import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASS,
    RABBITMQ_EXCHANGE,
    RABBITMQ_EXCHANGE_TYPE,
    RABBITMQ_ROUTING_KEY,
    RABBITMQ_DURABLE,
)
from resources.market.market_schema import StockPrice
import random
from datetime import datetime
from db.enums import StockSymbol

PRICE_RANGES = {
    StockSymbol.AAPL: (150.0, 200.0),
    StockSymbol.MSFT: (300.0, 350.0),
    StockSymbol.GOOG: (120.0, 150.0),
    StockSymbol.AMZN: (130.0, 160.0),
    StockSymbol.META: (250.0, 300.0),
}

def generate_market_data_for_symbol(symbol: StockSymbol) -> dict:
    current_time = datetime.now().isoformat()
    min_price, max_price = PRICE_RANGES[symbol]
    price = round(random.uniform(min_price, max_price), 2)
    
    return StockPrice(
        symbol=symbol.value,
        price=price,
        currency="USD",
        timestamp=current_time
    ).model_dump()

def publish_market_data(market_data: dict) -> None:
    connection = Connection(
        hostname=RABBITMQ_HOST,
        username=RABBITMQ_USER,
        password=RABBITMQ_PASS,
        port=RABBITMQ_PORT
    )
    
    try:
        channel = connection.channel()
        
        channel.basic.publish(
            exchange=RABBITMQ_EXCHANGE,
            routing_key=RABBITMQ_ROUTING_KEY,
            body=json.dumps(market_data),
        )
    finally:
        connection.close()

if __name__ == "__main__":
    while True:
        try:
            print("\nPublishing market data:")
            for symbol in StockSymbol:
                market_data = generate_market_data_for_symbol(symbol)
                print(f"{symbol.value}: ${market_data['price']}")
                publish_market_data(market_data)
            import time
            time.sleep(5)
        except KeyboardInterrupt:
            print("\nStopping market data publisher...")
            break

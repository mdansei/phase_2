"""RabbitMQ event subscriber for processing market data and generating alerts."""
import pika
import json
import sys
from contextlib import contextmanager
from db.config import get_db
import resources.alerts.alert_service as AlertService
from core.constants import (
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_USER,
    RABBITMQ_PASS,
    RABBITMQ_VHOST,
    RABBITMQ_QUEUE,
)

def callback(ch, method, properties, body):
    try:
        market_data = json.loads(body)
        print(f"\nReceived market data for {market_data['symbol']}: ${market_data['price']}")
        
        with contextmanager(get_db)() as session:
            AlertService.process_market_data(market_data, session)
            ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        ch.basic_nack(delivery_tag=method.delivery_tag)
        print(f"Error processing message: {e}")

def main():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            virtual_host=RABBITMQ_VHOST,
            credentials=credentials
        )
    )
    channel = connection.channel()

    print(f"Waiting for market data on queue {RABBITMQ_QUEUE}. To exit press CTRL+C")
    channel.basic_consume(
        queue=RABBITMQ_QUEUE,
        on_message_callback=callback,
        auto_ack=False
    )

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nShutting down...")
        channel.stop_consuming()
    finally:
        connection.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)

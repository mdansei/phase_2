"""Project-wide configuration constants."""
import os

DB_DRIVER = os.getenv("DB_DRIVER", "cockroachdb")
DB_USER = os.getenv("DB_USER", "root")
DB_HOST = os.getenv("DB_HOST", "database")
DB_PORT = os.getenv("DB_PORT", "26257")
DB_NAME = os.getenv("DB_NAME", "investor_bulletin")

DATABASE_URL = f"{DB_DRIVER}://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=disable"

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "broker")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "/")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "alerts")
RABBITMQ_EXCHANGE_TYPE = os.getenv("RABBITMQ_EXCHANGE_TYPE", "topic")
RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "threshold.alert")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "alerts_queue")
RABBITMQ_DURABLE = os.getenv("RABBITMQ_DURABLE", "true").lower() == "true"

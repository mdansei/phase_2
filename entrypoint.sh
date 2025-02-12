#!/bin/sh

check_db() {
    psql "postgres://${DB_USER}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=disable" -c "SELECT 1" >/dev/null 2>&1
}

echo "Waiting for database to be ready..."
while ! check_db; do
    echo "Database is unavailable - sleeping"
    sleep 2
done

echo "Database is ready!"

echo "Running database migrations..."
alembic upgrade head

echo "Starting the application..."
exec "$@"

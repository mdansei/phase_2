from uvicorn import run
from fastapi import FastAPI
from api.routes import init_routes


app = init_routes(FastAPI())

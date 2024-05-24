from fastapi import FastAPI
from app.views.addition_view import api_router
from app.utils.monitoring import start_monitoring_server

app = FastAPI()

app.include_router(api_router)

# Start Prometheus monitoring server
start_monitoring_server()

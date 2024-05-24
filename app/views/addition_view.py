from fastapi import APIRouter
from app.controllers.addition_controller import router as addition_router

api_router = APIRouter()
api_router.include_router(addition_router)

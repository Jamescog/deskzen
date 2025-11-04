from fastapi import APIRouter

user_router = APIRouter(prefix="/v1/users", tags=["users"])
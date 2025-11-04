from fastapi import FastAPI

from user_service.routes import user_router


app = FastAPI(
    title="User Service",
    description="Service for managing users, authentication, and roles.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations related to user management"
        }
    ],
)

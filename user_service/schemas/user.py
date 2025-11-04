from enum import Enum
from pydantic import BaseModel, EmailStr, Field
from sympy import true




class UserRoleEnum(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"
    MANAGER = "manager"


class UserCreateSchema(BaseModel):
    email: EmailStr = Field(..., description="The user's email address")
    password: str = Field(..., min_length=8, description="The user's password")
    full_name: str = Field(..., max_length=100, description="The user's full name")
    role: UserRoleEnum = Field(..., description="The user's role", default=UserRoleEnum.EMPLOYEE)

    
    class Config:
        json_schema_extra = {
            "examples": [{
                "email": "abebemola@example.com",
                "password": "strongpassword123",
                "full_name": "Abebe Mola Kassa",
                "role": "employee"
            },
            {
                "email": "kebede@example.com",
                "password": "anotherstrongpassword123",
                "full_name": "Kebede Abebe Hailu",
                "role": "manager"
            }]
        }


class UserResponseSchema(BaseModel):
    id: int = Field(..., description="The user's ID")
    email: EmailStr = Field(..., description="The user's email address")
    full_name: str = Field(..., description="The user's full name")
    is_active: bool = Field(..., description="Indicates if the user is active")
    role: UserRoleEnum = Field(..., description="The user's role")
    created_at_utc: str = Field(..., description="Account creation time in UTC")
    updated_at_utc: str = Field(..., description="Last account update time in UTC")
    created_at_ethiopian: str = Field(..., description="Account creation time in Ethiopian time")
    updated_at_ethiopian: str = Field(..., description="Last account update time in Ethiopian time")

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "email": "abebemola@example.com",
                "full_name": "Abebe Mola Kassa",
                "is_active": True,
                "role": "employee",
                "created_at_utc": "2023-01-01T00:00:00Z",
                "updated_at_utc": "2023-01-01T00:00:00Z",
                "created_at_ethiopian": "2023-01-01T03:00:00+03:00",
                "updated_at_ethiopian": "2023-01-01T03:00:00+03:00"
            }
        }


class UserLoginRequestSchema(BaseModel):
    email: EmailStr = Field(..., description="The user's email address")
    password: str = Field(..., description="The user's password")

    class Config:
        json_schema_extra = {
            "example": {
                "email": "abebemola@example.com",
                "password": "strongpassword123"
            }
        }


class UserLoginResponseSchema(BaseModel):
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(..., description="Type of the token, typically 'bearer'")
    user: UserResponseSchema = Field(..., description="The logged-in user's details")

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "user": {
                    "id": 1,
                    "email": "abebemola@example.com",
                    "full_name": "Abebe Mola Kassa",
                    "is_active": True,
                    "role": "employee",
                    "created_at_utc": "2023-01-01T00:00:00Z",
                    "updated_at_utc": "2023-01-01T00:00:00Z",
                    "created_at_ethiopian": "2023-01-01T03:00:00+03:00",
                    "updated_at_ethiopian": "2023-01-01T03:00:00+03:00"
                }
            }
        }
from datetime import datetime, timedelta, timezone
from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, func, Boolean, Enum as SQLEnum

from user_service.database import Base
from user_service.utils import get_current_utc_time, get_current_ethiopian_time


class UserRoleEnum(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"
    MANAGER = "manager"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    department_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    role: Mapped[UserRoleEnum] = mapped_column(SQLEnum(UserRoleEnum), default=UserRoleEnum.EMPLOYEE, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=get_current_utc_time, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=get_current_utc_time, onupdate=get_current_utc_time, nullable=False)


    def __repr__(self) -> str:
        """String representation of the User instance."""
        return f"<User(id={self.id}, email={self.email}, role={self.role}, is_active={self.is_active})>"


    def to_dict(self) -> dict:
        """Convert User instance to dictionary including both UTC and Ethiopian timestamps."""
        return {
            "id": self.id,
            "email": self.email,
            "full_name": self.full_name,
            "department_id": self.department_id,
            "role": self.role,
            "is_active": self.is_active,
            "created_at_utc": self.created_at.isoformat(),
            "updated_at_utc": self.updated_at.isoformat(),
            "created_at_ethiopian": get_current_ethiopian_time(self.created_at).isoformat(),
            "updated_at_ethiopian": get_current_ethiopian_time(self.updated_at).isoformat(),
        }



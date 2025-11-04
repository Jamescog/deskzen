from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime

from user_service.database import Base
from user_service.utils import get_current_ethiopian_time


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    floor_assignment: Mapped[str | None] = mapped_column(String(255), nullable=True)
    max_capacity: Mapped[int | None] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=get_current_ethiopian_time, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=get_current_ethiopian_time, onupdate=get_current_ethiopian_time, nullable=False)

    def __repr__(self) -> str:
        """String representation of the Department instance."""
        return f"<Department(id={self.id}, name={self.name}, floor_assignment={self.floor_assignment}, max_capacity={self.max_capacity})>"

    def to_dict(self) -> dict:
        """Convert Department instance to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "floor_assignment": self.floor_assignment,
            "max_capacity": self.max_capacity,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }



from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, DateTime, Boolean, Text

from user_service.database import Base
from user_service.utils import get_current_ethiopian_time, get_current_utc_time


class UserPreference(Base):
    __tablename__ = "user_preferences"

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    preferred_floor: Mapped[str | None] = mapped_column(String(255), nullable=True)
    preferred_zone: Mapped[str | None] = mapped_column(String(255), nullable=True)
    notification_email: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    notification_sms: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    quiet_workspace: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=get_current_utc_time, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=get_current_utc_time, onupdate=get_current_utc_time, nullable=False)

    def __repr__(self) -> str:
        """String representation of the UserPreference instance."""
        return f"<UserPreference(user_id={self.user_id}, preferred_floor={self.preferred_floor}, preferred_zone={self.preferred_zone})>"

    def to_dict(self) -> dict:
        """Convert UserPreference instance to dictionary."""
        return {
            "user_id": self.user_id,
            "preferred_floor": self.preferred_floor,
            "preferred_zone": self.preferred_zone,
            "notification_email": self.notification_email,
            "notification_sms": self.notification_sms,
            "quiet_workspace": self.quiet_workspace,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "created_at_ethiopian": get_current_ethiopian_time(self.created_at).isoformat(),
            "updated_at_ethiopian": get_current_ethiopian_time(self.updated_at).iso
        }
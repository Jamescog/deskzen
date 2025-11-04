from datetime import datetime, timedelta, timezone


def get_current_utc_time() -> datetime:
    """Get the current UTC time."""
    return datetime.now(timezone.utc)

def get_current_ethiopian_time() -> datetime:
    """Get the current Ethiopian time."""
    ethiopian_offset = timedelta(hours=3)
    return datetime.now(timezone.utc) + ethiopian_offset

def ethiopian_time_to_utc(ethiopian_time: datetime) -> datetime:
    """Convert Ethiopian time to UTC."""
    ethiopian_offset = timedelta(hours=3)
    return ethiopian_time - ethiopian_offset

def utc_time_to_ethiopian(utc_time: datetime) -> datetime:
    """Convert UTC time to Ethiopian time."""
    ethiopian_offset = timedelta(hours=3)
    return utc_time + ethiopian_offset
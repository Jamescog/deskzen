from datetime import datetime, timedelta, timezone



def get_current_utc_time() -> datetime:
    return datetime.now(timezone.utc)

def get_current_ethiopian_time() -> datetime:
    ethiopian_offset = timedelta(hours=3)
    return datetime.now(timezone.utc) + ethiopian_offset

def ethiopian_time_to_utc(ethiopian_time: datetime) -> datetime:
    ethiopian_offset = timedelta(hours=3)
    return ethiopian_time - ethiopian_offset

def utc_time_to_ethiopian(utc_time: datetime) -> datetime:
    ethiopian_offset = timedelta(hours=3)
    return utc_time + ethiopian_offset
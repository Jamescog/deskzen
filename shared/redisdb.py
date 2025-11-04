import os

from redis.asyncio import Redis

REQUIRED_ENV_VARIABLES = {
    "REDIS_HOST":"REDIS_HOST",
    "REDIS_PORT":"REDIS_PORT",
    "REDIS_DB":"REDIS_DB",
}

for key, var in REQUIRED_ENV_VARIABLES.items():
    if var not in os.environ:
        raise EnvironmentError(f"Required environment variable '{var}' is not set.")

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = os.environ["REDIS_PORT"]
REDIS_DB = os.environ["REDIS_DB"]

rdb = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
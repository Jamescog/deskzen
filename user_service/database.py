import os
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase


REQUIRED_ENV_VARIABLES = {
    "USER_DB_NAME":"USER_DB_NAME",
    "USER_DB_USER_NAME":"USER_DB_USER_NAME",
    "USER_DB_PASSWORD":"USER_DB_PASSWORD"
}

for key, var in REQUIRED_ENV_VARIABLES.items():
    if var not in os.environ:
        raise EnvironmentError(f"Required environment variable '{var}' is not set.")


USER_DB_NAME = os.environ["USER_DB_NAME"]
USER_DB_USER_NAME = os.environ["USER_DB_USER_NAME"]
USER_DB_PASSWORD = os.environ["USER_DB_PASSWORD"]


class Base(DeclarativeBase):
    pass


USER_DATABASE_URL = f"mysql+aiomysql://{USER_DB_USER_NAME}:{USER_DB_PASSWORD}@localhost:3306/{USER_DB_NAME}"

async_engine = create_async_engine(USER_DATABASE_URL, echo=False)

AsyncSessionLocal = async_sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)

async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session 

                                                                              
                                                 
DBSession = Annotated[AsyncSession, Depends(get_async_session)] 

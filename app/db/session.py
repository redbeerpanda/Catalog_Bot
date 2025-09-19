from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
from typing import AsyncGenerator


class Base(DeclarativeBase):
    pass


engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,  # True для отладки SQL запросов
    future=True,
)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


""" from typing import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession, None]: """

from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.settings import settings


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Get a database session using SQLAlchemy's async sessionmaker.

    Returns:
        An async generator that yields an AsyncSession object.

    Raises:
        SQLAlchemyError: If an error occurs during the session creation or commit.
    """
    engine = create_async_engine(settings.DATABASE_URL)
    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError:
            await session.rollback()
            raise

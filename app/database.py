from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


from app.config import DATABASE_URL

DB_URL = DATABASE_URL

engine = create_async_engine(DB_URL)

session = sessionmaker(bind = engine, class_ = AsyncSession, expire_on_commit = False)


class Base(DeclarativeBase):
    pass
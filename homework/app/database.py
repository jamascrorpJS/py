from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine 
from sqlalchemy.orm import DeclarativeBase, sessionmaker


db_url = 'postgresql+asyncpg://postgres:postgres@localhost:5432/postgres'

engine = create_async_engine(db_url)
session = sessionmaker(engine, class_=AsyncSession)

class Base(DeclarativeBase):
    pass
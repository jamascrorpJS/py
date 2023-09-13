from app.database import session
from sqlalchemy import select
class BaseDAO:
    model = None
    @classmethod




    async def find_by_id(cls, id:int):
        async with session() as s:
            query = select(cls.model).filter_by(id=id)
            bookings = await s.execute(query)
            return bookings.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        
        async with session() as s:
            query = select(cls.model).filter_by(**filter_by)
            bookings = await s.execute(query)
            return bookings.scalar_one_or_none()
    @classmethod
    async def find_all(cls, **filter_by):
        
        async with session() as s:
            query = select(cls.model).filter_by(**filter_by)
            bookings = await s.execute(query)
            return bookings.scalars().all()
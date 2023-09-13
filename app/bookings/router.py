from fastapi import APIRouter
from sqlalchemy import select, text
from app.bookings.dao import BookingDAO
from app.bookings.models import Bookings

from app.database import session

router = APIRouter(prefix='/bookings', tags=['Bookings'])

@router.get('')
async def get_bookings():
    return await BookingDAO.find_all()
    # async with session() as s:
        # res = await s.execute(text('SELECT * FROM bookings WHERE id=1'))
        # fetch = res.fetchall()

        # column_names = res.keys()

        # data = [dict(zip(column_names, row)) for row in fetch]
        # return data
        
        
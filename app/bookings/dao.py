from app.database import session
from sqlalchemy import select
from app.bookings.models import Bookings
from app.dao.base import BaseDAO

class BookingDAO(BaseDAO):
    model = Bookings
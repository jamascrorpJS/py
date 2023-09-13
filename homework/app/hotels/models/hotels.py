from sqlalchemy import Column, Integer, String
from app.database import Base

class Hotels(Base):
    __tablename__= 'hotels'


 
 
    id = Column(Integer, primary_key=True)
    room = Column(String)

from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel
from app.bookings.router import router as router_bookings

app = FastAPI()

app.include_router(router_bookings)

class body(BaseModel):
    s:int
    x:str

@app.get('/s/{s}')
def get_pizza(
    s: int,
    x: Optional[str] = None
    
) -> body:
    return body(s=s,x=x)


@app.post('/sx')
def getsx(Sx:body):
    pass
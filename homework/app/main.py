from typing import Optional
from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class cls(BaseModel):
    stroka: str
    cislo: Optional[int] = None

@app.post('/ex')
def ex(s: cls):

    return s
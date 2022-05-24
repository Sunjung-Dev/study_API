from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from database.db_conn import engineconn
from database.db_class import Test

#인스턴스 생성 부분
app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

class Item(BaseModel):
    id : int
    password : str

@app.get("/")
async def first_get():
    example = session.query(Test).all()
    return example

@app.get("/post")
async def first_post(item:Item):
    return item



#uvicorn main:app --reload: api 실행시키는 것 
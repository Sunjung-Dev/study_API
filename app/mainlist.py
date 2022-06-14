from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
#파이썬에서 html을 사용하는 템플릿
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import requests

app = FastAPI()

db = []

# data model 정의
class City(BaseModel):
    name: str
    timezone: str

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/cities', response_class=HTMLResponse)
def get_cities(request: Request):

    context = {}
    
    rsCity = []
    
    for city in db:
        str = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        print(str)
        r = requests.get(str)
        cur_time = r.json()['datetime']
        rsCity.append({'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time})
    
    context['request'] = request
    context['raCity'] = rsCity
    return templates.TemplateResponse('city_list.html', context)


@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city = db[city_id-1]
    r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
    cur_time = r.json()['datetime']
    return {'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}


@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}





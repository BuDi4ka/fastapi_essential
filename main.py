from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    name: str
    age: int | None

@app.get('/')
async def root(name: str, age: int):
    return {'message': f'Hello {name}, {age}!'}

@app.post('/{name}')
async def post(users: list[User] | None):
    if users is None:
        users = []
    names = [user.name for user in users]
    return {'message': f'Hello {', '.join(names)}!'}


@app.get('/user/{user_id}')
async def get_user(name):
    return {'user_id': name}

@app.post('/user/')
async def create_user(user: User):
    return {'user': user}

@app.put('/user/{user_id}')
async def update_user(user_id: int, user: User):
    return {'user_id': user_id, 'user': user}

@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    return {'user_id': user_id, 'message': 'User deleted'}


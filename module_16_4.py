from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_new_user(username: str, age: int) -> User:
    if len(users):
        new_index = users[-1].id + 1
    else:
        new_index = 1
    new_user = User(id=new_index, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        current_index = [x.id for x in users].index(user_id)
        users[current_index].username = username
        users[current_index].age = age
        return users[current_index]
    except ValueError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        current_index = [x.id for x in users].index(user_id)
        removed_user = users.pop(current_index)
        return removed_user
    except ValueError:
        raise HTTPException(status_code=404, detail="User was not found")

from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_new_user(username: str, age: int) -> str:
    new_index = sorted(map(int, users.keys()))[-1] + 1
    users[str(new_index)] = f'Имя: {username}, возраст: {age}'
    return f'User {new_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'

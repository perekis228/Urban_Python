#uvicorn main:app --reload
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='Eva'),
                      age: int = Path(ge=18, le=120, description='Enter age', example=20)) -> str:
    cur_id = str(int(max(users, key=int))+1)
    users[cur_id] = f"Имя: {username}, возраст: {age}"
    return f"User {cur_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str = Path(max_length=10, description='Enter user id', example='1'),
                      username: str = Path(min_length=5, max_length=20, description='Enter username', example='Eva'),
                      age: int = Path(ge=18, le=120, description='Enter age', example=20)) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str = Path(max_length=10, description='Enter user id', example='1')) -> str:
    del users[user_id]
    return f"User {user_id} has been deleted"

#uvicorn main:app --reload
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List
from typing import Annotated

app = FastAPI()
users = {}

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/users")
async def all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def create_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='Eva'),
                      age: int = Path(ge=18, le=120, description='Enter age', example=20)) -> User:
    cur_id = len(users)
    users.append(User(id=cur_id, username=username, age=age))
    return users[cur_id]

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int = Path(description='Enter user id', example=1),
                      username: str = Path(min_length=5, max_length=20, description='Enter username', example='Eva'),
                      age: int = Path(ge=18, le=120, description='Enter age', example=20)) -> str:

    for num, user in enumerate(users):
        if user.id == user_id:
            users[num] = User(id=user_id, username=username, age=age)
            return f'User {user_id} has been updated'
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(description='Enter user id', example=1)) -> User:
    for num, user in enumerate(users):
        if user.id == user_id:
            del_user = users.pop(num)
            return del_user
    raise HTTPException(status_code=404, detail='User was not found')

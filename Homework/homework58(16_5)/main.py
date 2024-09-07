#uvicorn main:app --reload
from fastapi import FastAPI, Path, HTTPException, status, Body, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from typing import Annotated
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/")
async def main(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get("/users/{user_id}")
async def all_users(request: Request, user_id: int = Path(description='Enter user id', example=1)) -> HTMLResponse:
    cur_user = None
    for num, user in enumerate(users):
        if user.id == user_id:
            cur_user = users[num]
            break
    return templates.TemplateResponse('users.html', {'request': request, 'user': cur_user})

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
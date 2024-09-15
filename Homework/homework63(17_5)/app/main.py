#uvicorn main:app --reload
#python -m uvicorn main:app
from fastapi import FastAPI
from app.routers import task, user

App = FastAPI()

@App.get('/')
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}


App.include_router(task.router)
App.include_router(user.router)
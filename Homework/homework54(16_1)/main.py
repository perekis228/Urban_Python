#uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_number(user_id: int = 0) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def user_info(username: str = "Alex", age: int = 20) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

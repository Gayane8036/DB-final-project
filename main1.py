from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from typing import List

app = FastAPI()


# Подключение к базе данных PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",  # адрес базы данных (если база в Docker, это localhost)
        port="5432",  # порт PostgreSQL
        database="postgres",  # имя базы данных
        user="postgres",  # пользователь
        password="mysecretpassword"  # пароль
    )
    return conn


# Модель данных для пользователя
class User(BaseModel):
    id: int
    name: str
    email: str


# Получить всех пользователей
@app.get("/users", response_model=List[User])
async def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    # Преобразуем данные в список словарей
    return [{"id": user[0], "name": user[1], "email": user[2]} for user in users]


# Добавить нового пользователя
@app.post("/users")
async def add_user(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "User added successfully!"}

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int]
    created_at: Optional[date]

users = [
    User(id=1, name="John Doe", email="john@example.com"),
    User(id=2, name="Jane Doe", email="jane@example.com"),
    User(id=3, name="Alice Smith", email="alice@example.com")
]

@app.get("/users/")
async def read_users():
    return users

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {}

@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for i, u in enumerate(users):
        if u.id == user_id:
            users[i] = user
            return user
    return {}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return {"message": f"User {user_id} deleted"}
    return {}
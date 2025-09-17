from sqlmodel import Field, Session, SQLModel, select
from fastapi import FastAPI
from database import create_db_and_tables, get_session
from model import User, Product

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/users/")
def create_user(u: User):

    with next(get_session()) as session:
        existing_user = session.exec(select(User).where(User.email == u.email)).first()
        if existing_user:
            return {"error": "Email already registered"}
        session.add(u)
        session.commit()
        session.refresh(u)
        return u

@app.get("/users/")
def read_users():
    with next(get_session()) as session:
        users = session.exec(select(User)).all()
        return users

@app.get("/user/{user_id}")
def read_user(user_id: int):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.id == user_id)).first()
        if user:
            return user
        return {"error": "User not found"}


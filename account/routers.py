from fastapi import APIRouter
from model import User, LoginUser
from database import get_session
from sqlmodel import select


account_router = APIRouter()


@account_router.post("/users/")
def create_user(u: User):

    with next(get_session()) as session:
        existing_user = session.exec(select(User).where(User.email == u.email)).first()
        if existing_user:
            return {"error": "Email already registered"}
        session.add(u)
        session.commit()
        session.refresh(u)
        return u

@account_router.get("/users/")
def read_users():
    with next(get_session()) as session:
        users = session.exec(select(User)).all()
        return users

@account_router.get("/user/{user_id}")
def read_user(user_id: int):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.id == user_id)).first()
        if user:
            return user
        return {"error": "User not found"}

@account_router.post("/login")
def login(user: LoginUser):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.email == user.email and User.password == user.password)).first()
        if user:
            return {"message": "Login successful"}
        return {"error": "Invalid email or password"}
    
@account_router.get("/login")
def login_user(userId: int, password: str):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.id == userId and User.password == password)).first() # select * from user where id = userId and password = password
        if user:
            return {"message": "Login successful"}
        return {"error": "Invalid email or password"}   
    
@account_router.post("/loginUser")
def login_user(userId: int, password: str):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.id == userId and User.password == password)).first() # select * from user where id = userId and password = password
        if user:
            return {"message": "Login successful"}
        return {"error": "Invalid email or password"}
    
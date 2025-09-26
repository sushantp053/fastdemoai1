from sqlmodel import Field, Session, SQLModel, select
from fastapi import FastAPI
from database import create_db_and_tables, get_session
from model import User, Product, LoginUser, Category
from account.routers import account_router  
from product.routers import router as product_router
from address import router as address_router

app = FastAPI(openapi_prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}
app.include_router(account_router, prefix="/account",  tags=["account"])
app.include_router(product_router, prefix="/product", tags=["product"])
app.include_router(address_router, prefix="/address", tags=["address"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

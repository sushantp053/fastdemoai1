from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str 
    email: str = Field(unique=True)
    password: str

class LoginUser(SQLModel, table=False):
    email: str
    password: str


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    user_id: int = Field(foreign_key="user.id")
    updated_at: str = Field(default=None)
    created_at: str = Field(default=None)

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    in_stock: bool
    user_id: int = Field(foreign_key="user.id")
    category_id: int = Field(foreign_key="category.id")

class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="product.id")
    quantity: int
    total_price: float
    status: str
    order_date: str = Field(default=None)
    updated_at: str = Field(default=None)
    created_at: str = Field(default=None)

class Stock(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id", unique=True)
    quantity: int
    last_updated: str = Field(default=None)
    updated_at: str = Field(default=None)
    created_at: str = Field(default=None)



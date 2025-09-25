from sqlmodel import Field, Session, SQLModel, select
from fastapi import FastAPI
from database import create_db_and_tables, get_session
from model import User, Product, LoginUser, Category

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

@app.post("/login")
def login(user: LoginUser):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.email == user.email and User.password == user.password)).first()
        if user:
            return {"message": "Login successful"}
        return {"error": "Invalid email or password"}
    
@app.get("/login")
def login_user(userId: int, password: str):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.id == userId and User.password == password)).first() # select * from user where id = userId and password = password
        if user:
            return {"message": "Login successful"}
        return {"error": "Invalid email or password"}   
    
@app.post("/loginUser")
def login_user(userId: int, password: str):
    with next(get_session()) as session:
        user = session.exec(select(User).where(User.id == userId and User.password == password)).first() # select * from user where id = userId and password = password
        if user:
            return {"message": "Login successful"}
        return {"error": "Invalid email or password"}
    
@app.post("/category")
def create_category(category: Category):
    with next(get_session()) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category
    
@app.get("/categories/")
def read_categories():
    with next(get_session()) as session:
        categories = session.exec(select(Category)).all()
        return categories

@app.post("/product/")
def create_product(product: Product):
    with next(get_session()) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product
    
@app.get("/products/")
def read_products():
    with next(get_session()) as session:
        products = session.exec(select(Product)).all()
        return products

@app.get("/product/{product_id}")
def read_product(product_id: int):
    with next(get_session()) as session:
        product = session.exec(select(Product).where(Product.id == product_id)).first()
        if product:
            return product
        return {"error": "Product not found"}
    

@app.get("/products_with_category/")
def read_products_with_category():
    with next(get_session()) as session:
        statement = select(Product, Category).join(Category, Product.category_id == Category.id)
        results = session.exec(statement).all()
        print(results)
        products_with_categories = [
            {"product_id": product.id, 
             "product_name": product.name,
             "product_price": product.price,
             "category_id": category.id, 
             "category_name": category.name
         } for product, category in results]
        return products_with_categories

@app.get("/products_in_category_username")
def read_products_in_category_username():
    with next(get_session()) as session:
        statement = select(Product, Category, User).join(Category, Product.category_id == Category.id).join(User, Product.user_id == User.id)
        results = session.exec(statement).all()
        print(statement)
        products_in_category_username = [
            {"product_id": product.id, 
             "product_name": product.name,
             "product_price": product.price,
             "category_id": category.id,
             "category_name": category.name,
             "user_id": user.id,
             "user_name": user.name
             } for product, category, user in results]
        return products_in_category_username

@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    with next(get_session()) as session:
        product = session.exec(select(Product).where(Product.id == product_id)).first()
        if product:
            session.delete(product)
            session.commit()
            return {"message": "Product deleted successfully"}
        return {"error": "Product not found"}
    return {"error": "Product not found"}

@app.put("/product/{product_id}")
def update_product(product_id: int, updated_product: Product):
    with next(get_session()) as session:
        product = session.exec(select(Product).where(Product.id == product_id)).first()
        if product:
            product.name = updated_product.name
            product.price = updated_product.price
            product.category_id = updated_product.category_id
            session.commit()
            return {"message": "Product updated successfully"}
        return {"error": "Product not found"}
    
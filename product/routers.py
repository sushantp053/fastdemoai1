from fastapi import APIRouter
from database import get_session
from model import Product, Category
from sqlmodel import select

router = APIRouter()


@router.post("/category")
def create_category(category: Category):
    with next(get_session()) as session:
        session.add(category)
        session.commit()
        session.refresh(category)
        return category
    
@router.get("/categories/")
def read_categories():
    with next(get_session()) as session:
        categories = session.exec(select(Category)).all()
        return categories

@router.post("/product/")
def create_product(product: Product):
    with next(get_session()) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product
    
@router.get("/products/")
def read_products():
    with next(get_session()) as session:
        products = session.exec(select(Product)).all()
        return products

@router.get("/product/{product_id}")
def read_product(product_id: int):
    with next(get_session()) as session:
        product = session.exec(select(Product).where(Product.id == product_id)).first()
        if product:
            return product
        return {"error": "Product not found"}
    

@router.get("/products_with_category/")
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

@router.get("/products_in_category_username")
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

@router.delete("/product/{product_id}")
def delete_product(product_id: int):
    with next(get_session()) as session:
        product = session.exec(select(Product).where(Product.id == product_id)).first()
        if product:
            session.delete(product)
            session.commit()
            return {"message": "Product deleted successfully"}
        return {"error": "Product not found"}
    return {"error": "Product not found"}

@router.put("/product/{product_id}")
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
    

import streamlit as st
import requests

response = requests.get("http://localhost:8000/categories/")
categories = []
if response.status_code == 200:
    categories = response.json()

st.subheader("Add New Product")

with st.form("product_form"):
    st.text_input("Product Name", key="product_name")
    st.text_area("Product Description", key="product_description")
    st.text_input("Price", key="price")
    st.checkbox("In Stock", key="in_stock")
    st.selectbox("Category", options=[cat['id'] for cat in categories], key="category_id")
    st.text_input("User ID", key="user_id")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if (st.session_state.product_name and st.session_state.product_description and 
            st.session_state.category_id and st.session_state.user_id and st.session_state.price):
            
            product_data = {
                "name": st.session_state.product_name,
                "description": st.session_state.product_description,
                "category_id": int(st.session_state.category_id),
                "user_id": int(st.session_state.user_id),
                "price": float(st.session_state.price),
                "in_stock": bool(st.session_state.in_stock)
            }
            response = requests.post("http://localhost:8000/product/", json=product_data)

            if response.status_code == 200:
                st.success("Product created successfully!")
            else:
                st.error("Error creating product.")
        else:
            st.error("Please fill in all required fields.")
import streamlit as st
import requests

st.subheader("Add New Category")

with st.form("category_form"):
    st.text_input("Category Name", key="category_name")
    st.text_area("Category Description", key="category_description")
    st.text_input("User ID", key="user_id")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if st.session_state.category_name and st.session_state.category_description and st.session_state.user_id:
            
            category_data = {
                "name": st.session_state.category_name,
                "description": st.session_state.category_description,
                "user_id": int(st.session_state.user_id),
                "updated_at": "demo",
                "created_at": "demo"
            }
            response = requests.post("http://localhost:8000/category", json=category_data)

            if response.status_code == 200:
                st.success("Category created successfully!")
            else:
                st.error("Error creating category.")


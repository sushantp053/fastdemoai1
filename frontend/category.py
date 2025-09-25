import streamlit as st
import requests


st.title("Category List")

response = requests.get("http://localhost:8000/categories/")
if response.status_code == 200:
    categories = response.json()
    st.divider()
    for category in categories:
        st.write(f"{category['name']}: {category['description']}")
        st.divider()
else:
    st.error("Error fetching categories.")
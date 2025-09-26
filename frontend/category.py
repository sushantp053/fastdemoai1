import streamlit as st
import requests
import const


st.title("Category List")

response = requests.get(f"{const.api_base_url}/categories/")
if response.status_code == 200:
    categories = response.json()
    st.divider()
    for category in categories:
        st.write(f"{category['name']}: {category['description']}")
        st.divider()
else:
    st.error("Error fetching categories.")
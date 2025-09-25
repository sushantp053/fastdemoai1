import streamlit as st
import requests

pages = {
    "Your account": [
        st.Page("create_category.py", title="Create new category"),
        st.Page("create_product.py", title="Create new product"),
    ],
    "Resources": [
        st.Page("category.py", title="Categories"),
        st.Page("product.py", title="Products"),
    ],
}


pg = st.navigation(pages)
pg.run()

import streamlit as st 

pages = [
    st.Page("pages/home.py", title = "Home")
]

pg = st.navigation(pages)

pg.run()

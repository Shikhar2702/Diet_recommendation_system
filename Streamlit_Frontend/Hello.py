import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Diet Recommendation System! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A diet recommendation web application using content-based approach with Scikit-Learn and FastAPI.
    Final year major project by -  
    Shikhar Agrawal
    Sachin Kumar Singh
    Shruti Sharma
    Yanshi Gupta
    """
)

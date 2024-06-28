import streamlit as st
import dashboard
import classifyDeep

st.set_page_config(
    page_title="The Deep Roy",
    page_icon="🍆",
    layout="wide")

PAGES = {
    "Dashboard": dashboard,
    "The Deep Fake": classifyDeep
}

st.sidebar.title("The Deep Roy: Deepfake Detection")

st.sidebar.write("Satria H. Sulistyo | 3IA01 | 51421396")

selection = st.sidebar.radio("Navigation:", list(PAGES.keys()))

page = PAGES[selection]

page.app()

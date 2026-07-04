import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="centered"
)

# Read your HTML file
with open("main.html", "r", encoding="utf-8") as f:
    html = f.read()

# Display the HTML
components.html(html, height=700, scrolling=True)

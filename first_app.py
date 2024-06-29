
import streamlit as st

st.title("my first streamlit app")

st.write("welcome to my streamlite app")

st.button("reset", type="primary")
if st.button("say hello"):
  st.write("why hello there")

else:
  st.write("goodbye")

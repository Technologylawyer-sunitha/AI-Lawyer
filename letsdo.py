import streamlit as st

st.title("AI-Lawyer")
st.write ("AI-Lawyer is a platform to draft, review and manage contracts, as well as handle legal & finance compliances with ease")

st.sidebar.write("Finance")
st.sidebar.write("Legal")
st.file_uploader("Upload a file", type=["pdf", "docx"])

st.write("OR")

st.text_area("Paste your full contract or clause here", height=200)

st.button("Submit")

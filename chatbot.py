from funs import chat_with_deepseek
import streamlit as st



msg = st.text_input('please write your msg: ')

if st.button('click to get msg'):
    response = chat_with_deepseek(msg)
    st.header('user:')
    st.write(msg)
    st.header('chatbot')
    st.write(response)
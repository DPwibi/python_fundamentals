import streamlit as st
import random
from funs import rock_paper_scissors

options = ('rock', 'paper', 'scissors')
computer = random.choice(options)

user = st.text_input('write your option: ')
result = rock_paper_scissors(computer,user)

mybutton = st.button('enter to get result')
if mybutton:
    st.write(f'{result} won')
    st.write(f'computer chose {computer}')

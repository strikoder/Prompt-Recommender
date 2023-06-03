import openai
import streamlit as st
from utils import get_ideal_prompt, print_outputs

"""
hide_st_style = 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>

st.markdown(hide_st_style, unsafe_allow_html=True)
"""

st.title('Act as GPT')

psw_col, sel_col = st.columns([2, 1])

OPENAI_API_KEY = psw_col.text_input("OpenAI API key", type='password')

model = sel_col.selectbox(
    'Model',
    ('gpt-3.5-turbo', 'gpt-4'))

st.write('\n')
st.write('\n')

max_tokens = st.slider('How many tokens?', 50, 400, 150)

user_input = st.text_input('Type input here')
st.write('Act as:', user_input)

if user_input != "":
    openai.api_key = OPENAI_API_KEY

    # predicting the input
    modified_input = get_ideal_prompt(user_input, 150)
    input_area = st.text_area("modified_input", value=modified_input, key="text_area", height=200)
    but_col1, _, _, _ = st.columns([1, 1, 1, 1])
    write_col1, write_col2, write_col3 = st.columns([1, 1, 1])

    if but_col1.button("Run"):
        print_outputs(input_area, user_input, model, write_col1, write_col2, write_col3)

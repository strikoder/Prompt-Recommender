import openai
import streamlit as st
from utils import get_ideal_prompt, print_outputs

# Hide Streamlit elements
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title('Act as GPT')

# Input fields
OPENAI_API_KEY = st.text_input("OpenAI API key", type='password')
model = st.selectbox(
    'Model',
    ('gpt-3.5-turbo', 'gpt-4')
)

# Slider for tokens
max_tokens = st.slider('How many tokens?', 50, 400, 150)

# User input and display
user_input = st.text_input('Type input here')
st.write('Act as:', user_input)

if user_input != "":
    openai.api_key = OPENAI_API_KEY

    # Generate the ideal prompt based on user input
    predict_prompt = get_ideal_prompt(user_input, max_tokens)

    # Text area for modified input prompt
    prompt = st.text_area("Modified Input", value=predict_prompt, key="text_area", height=200)

    # Columns for buttons and output display
    col1, col2, col3, _ = st.columns(4)

    if col1.button("Run"):
        print_outputs(prompt, user_input, model, col2, col3, col4)

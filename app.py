import openai
import streamlit as st
from utils import input_prompts, get_ideal_prompt, print_outputs




hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title('Act as GPT')

psw_col, sel_col = st.columns([2, 1])

OPENAI_API_KEY = psw_col.text_input("OpenAI API key", type='password')

model = sel_col.selectbox(
    'Model',
    ('gpt-3.5-turbo', 'gpt-4'))

st.write('\n')
st.write('\n')

# initilizing the selectbox with an empty element
input_prompts = [''] + input_prompts.tolist()

user_input = st.selectbox('Select an input prompt', input_prompts)
st.write('Act as:', user_input)
print(user_input)

if user_input != "":
    last_sentence = None
    sentences_counter = -1
    openai.api_key = OPENAI_API_KEY

    # Receiving input from the df
    modified_input = get_ideal_prompt(user_input)
    sentences = modified_input.split(".")

    # TODO: Debug all the dataset (gpt prompt generator+note taking+cheap+financial)

    # Find the last sentence containing the word "first"
    for sentence in reversed(sentences):
        if "first" in sentence.lower().split():
            last_sentence = sentence.strip()
            break
        else:
            sentences_counter -= 1

    if last_sentence:
        system_prompt = ". ".join(sentences[:1]) + "."
        input_text = ". ".join(sentences[1:sentences_counter]) + "." + last_sentence
        # Create a reactive text area with live update
        input_area = st.text_area("modified_input", value=input_text, key="text_area", height=200)

        but_col1, _, _, but_col2 = st.columns([1, 1, 1, 1])
        write_col1, write_col2, write_col3 = st.columns([1, 1, 1])

        if but_col1.button("Run"):
            print_outputs(input_area, system_prompt, model, write_col1, write_col2, write_col3)

import streamlit as st
from streamlit_ace import st_ace
import openai
from utils import input_prompts, get_completion, get_ideal_prompt

# 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

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

    # TODO: Debug all the dataset (gpt prompt generator)

    # Find the last sentence containing the word "first"
    for sentence in reversed(sentences):
        if "first" in sentence.lower().split():
            last_sentence = sentence.strip()
            break
        else:
            sentences_counter -= 1

    if last_sentence:
        input_first_half = ". ".join(sentences[:sentences_counter]) + "."
        st.write(input_first_half)
        # Create a reactive text area with live update
        input_second_half = st.text_area("modified_input", value=last_sentence + ".", key="text_area")
        input_text = input_first_half + input_second_half

        if st.button("Run"):
            # TODO: Add I want you to act as a sys input
            write_col1, write_col2, write_col3 = st.columns([1, 1, 1])
            output = get_completion(input_text, model)
            write_col1.write(output)
            output = get_completion(input_text, model)
            write_col2.write(output)
            output = get_completion(input_text, model)
            write_col3.write(output)

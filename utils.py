import streamlit as st
import openai
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoConfig
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


@st.cache_resource()
def LoadingModel():
    model = AutoModelForSeq2SeqLM.from_pretrained("K:\Github\ActasGPT\model\chatgpt-prompts", from_tf=True)
    tokenizer = AutoTokenizer.from_pretrained("K:\Github\ActasGPT\model\chatgpt-prompts")
    return model, tokenizer


model, tokenizer = LoadingModel()


def get_completion(
        prompt,
        system_prompt="You will act as an advanced language model. You will be given an input prompt from a user, your task is just to paraphrase the prompt, don't do anything else.",
        model="gpt-3.5-turbo"):
    """
    This function servers as a portal into Gpt API
    :param system_prompt:
    :param prompt:
    :param model:
    :return:
    """
    if not prompt:
        return prompt  # Return an empty string if the prompt is invalid
    # you will be provided with a prompt to act as someone or something, try to give the most ideal output for an unexpierienced user and epxlain everything from scratch
    messages = [
        {"role": "system",
         "content": f'I want you to act as a {system_prompt}'},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1,
    )
    return response.choices[0].message["content"]


def get_ideal_prompt(user_prompt, max_new_tokens=150):
    batch = tokenizer(user_prompt, return_tensors="pt")
    generated_ids = model.generate(batch["input_ids"], max_new_tokens)
    output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return output[0]


def print_outputs(input_text, system_prompt="", model='gpt-3.5-turbo', *args):
    for arg in args:
        output = get_completion(input_text, system_prompt, model)
        arg.write(output)

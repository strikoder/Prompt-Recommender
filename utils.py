import streamlit as st
import openai
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


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
    """
    Generate the ideal prompt based on the user input and maximum number of new tokens.
    Args:
        user_prompt (str): The user input.
        max_new_tokens (int): Maximum number of new tokens to predict the output prompt.

    Returns:
        str: The generated ideal prompt.
    """
    batch = tokenizer(user_prompt, return_tensors="pt")
    generated_ids = model.generate(batch["input_ids"], max_length=max_new_tokens)
    output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return output[0]


def print_outputs(input_text, system_prompt="", model='gpt-3.5-turbo', *args):
    """
     Print the outputs using the GPT API through the specified model and an internal function.

    Args:
        input_text (str): The input text.
        system_prompt (str): The system prompt.
        model (str): The GPT model to use.
        *args: Additional arguments for writing the output.
    """
    for arg in args:
        output = get_completion(input_text, system_prompt, model)
        arg.write(output)

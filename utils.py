import openai
import pandas as pd
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

prompts_df = pd.read_csv("model/prompts.csv")
input_prompts = prompts_df["act"]  # used in streamlit interface


def GPT_paraphrase(Input_prompt, model):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system",
             "content": "You will act as an advanced language model. The user wants you to paraphrase the provided input prompt to generate an ideal output."},
            {"role": "user", "content": Input_prompt}
        ],
        temperature=0,
    )
    return response.choices[0].message["content"]


def get_completion(
        prompt,
        system_prompt="You will act as an advanced language model. The user wants you to simulate the experience of interacting with the provided prompt.",
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
         "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=1,
    )
    return response.choices[0].message["content"]


def get_ideal_prompt(user_prompt):
    filtered_rows = prompts_df[prompts_df['act'].isin([user_prompt])]
    if not filtered_rows.empty:
        ideal_prompt = filtered_rows['prompt'].iloc[0]
        return ideal_prompt


def print_outputs(input_text, system_prompt="", model='gpt-3.5-turbo', *args):
    for arg in args:
        output = get_completion(input_text, system_prompt, model)
        arg.write(output)

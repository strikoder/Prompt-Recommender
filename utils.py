import openai
import pandas as pd
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

prompts_df = pd.read_csv("model/prompts.csv")

# showing only those prompts, which start with 'act' in the first sentence
input_prompts = prompts_df[prompts_df["prompt"].apply(lambda x: "act" in x.split(".")[0].lower())]["act"]

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

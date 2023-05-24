import pandas as pd
import openai

prompts_df = pd.read_csv("prompts.csv")
input_prompts = prompts_df["act"]  # used in streamlit interface



def get_ideal_prompt(user_prompt):
    print(user_prompt)
    filtered_rows = prompts_df[prompts_df['act'].isin([user_prompt])]
    if not filtered_rows.empty:
        ideal_prompt = filtered_rows['prompt'].iloc[0]
        return ideal_prompt


get_ideal_prompt("Travel Guide")


def get_completion(prompt, model="gpt-3.5-turbo"):
    if not prompt:
        return prompt  # Return an empty string if the prompt is invalid
    # you will be provided with a prompt to act as someone or something, try to give the most ideal output for an unexpierienced user and epxlain everything from scratch
    messages = [
        {"role": "system",
         "content": "You will act as an advanced language model. The user wants you to simulate the experience of interacting with the provided prompt."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.3,
    )
    return response.choices[0].message["content"]

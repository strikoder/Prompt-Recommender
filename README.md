# ActasGPT
 
ActasGPT is a project that aims to improve prompt prediction by utilizing the cosine_similarity(v1.0) and transformers(v2.0) techniques. The main objective of this project is to create a model that can accurately predict the most effective prompts for users, going beyond the limitations of the current database.
The transformer model is further refined and integrated into the project as part of a third-year project initiative.

## Table of Contents
* [Dataset](#Dataset)
* [Repo Structure](#Repo-Structure)
* [Technologies](#Technologies-Used)
* [Website Interface](#Website-Interface)
* [Improved Results](#Improved-Results)
* [Conclusion](#Conclusion)

## Dataset
The project utilizes the remarkable chatgpt prompts dataset:

* [Awesome chatgpt prompts](https://huggingface.co/datasets/fka/awesome-chatgpt-prompts)

The dataset comprises two columns: the input column, which acts as a prompt, and the output column.

## Repo Structure
The project has the following folders and files:

- imgs: includes images for the readme file
- model: houses the transformer model, the utilized dataset, and the notebooks used for training both the recent and initial versions of the program
- app.py: handles the website interface
- utils.py: provides the backend for the website, including the necessary functions and API calls


## Technologies Used
* matplotlib & wordcloud for data visiulization
* NLP for data-preprocessing
* transformers fine tuning & sklearn cosine similarity for model building in both versions
* GPT-API
* Streamlit for UI
* Amazon EC2 for cloud hosting

## Website Interface
The website features a simple and intuitive interface that enables users to input a prompt and receive predictions for the most suitable prompt that aligns with their request. The transformer model predicts the most appropriate prompt, which the user can then edit before final submission. Upon submission, the server connects with the GPT-API server and returns three different results, providing the user with a general idea of the prompt output and its efficiency.

### Old version:
![Interface V1.0](imgs/readme1.JPG)


## Improved Results
In the initial version, the model utilized cosine similarity, limiting its ability to predict prompts similar to those in the existing database, making it inefficient for real-time tasks. To address this, we fine-tuned a transformer model, primarily developed by [Merve](https://github.com/merveenoyan), to cater to our specific task. Additionally, the model was uploaded to the cloud using AWS.

![result1](imgs/readme2.JPG)
![result2](imgs/readme2.1.JPG)
![result3](imgs/readme2.2.JPG)




# Conclusion
This project successfully improves user input prompts, providing users with the opportunity to modify the generated prompt before submitting it to the GPT-API server. The resulting prompt outputs are then displayed, enhancing the prompt selection process.



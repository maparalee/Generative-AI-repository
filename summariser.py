# %%
from transformers import pipeline
import torch
import streamlit as st


#---FUNTION-----------

def summariser(text):

    pipe = pipeline(task='summarization' , model = 'facebook/bart-large-cnn')

    return pipe(text)






#---UI------------------
st.title('Summariser')

input_text = st.text_area('Enter the text', height=150)


response=''

if st.button('Summariser'):
    if input_text:
        response = summariser(input_text)
    else:
        response = 'Enter the text'

text_area = st.text_area('summarised text' , value=response ,height=150)


# %%
summariser(text)

# %%
pipe = pipeline(task='summarization' , model = 'facebook/bart-large-cnn')

# %%
text = f'''Definition: In standard prompting, you provide a prompt to the model, and it generates a response based on the patterns it has learned during training. The model is expected to respond based on its broad general knowledge but without any specific task framing. The prompt typically doesn't ask the model to solve a specific problem or use specialized knowledge that it has not encountered in training.'''


# %%
pipe(text,max_length=20)

# %%


# %%




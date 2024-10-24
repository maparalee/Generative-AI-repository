# %%
# !pip install streamlit

# %%
# pip show streamlit

# %%
import streamlit as st
from transformers import pipeline
import torch

#-------------Function----------------------
def translator(text):
    # Create a translation pipeline
    pipe = pipeline(task='translation', model="facebook/nllb-200-distilled-600M", torch_dtype=torch.bfloat16)

    # Perform translation
    response = pipe(text, src_lang='eng_Latn', tgt_lang='hin_Deva')
    
    # Return the translated text (response is a list of dictionaries)
    return response[0]['translation_text'] if response else "Translation failed."

#------------UI ----------------------

st.title('Translator')

# Create a text area for input
input_text = st.text_area("Enter text to translate", height=150)

# Initialize `translated_text` to an empty string (default value before translation)
translated_text = ""

# Create a button in the middle
if st.button("Translate"):
    if input_text:
        # Call the translator function
        translated_text = translator(input_text)
    else:
        translated_text = "Please enter some text to translate."

# Create another text area to display the result
st.text_area("Translated text", value=translated_text, height=150)


# %%


# %%


# %%


# %%






# %%
import streamlit as st
from transformers import BlipForConditionalGeneration, AutoProcessor
from PIL import Image

# Load model and processor
model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
processor = AutoProcessor.from_pretrained('Salesforce/blip-image-captioning-base')

# Streamlit app
st.title("Image Captioning with BLIP")

# File uploader to accept image from user
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file :
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Process the image when 'Caption' button is pressed
    if st.button('Generate Caption'):
        # Prepare image for model
        inputs = processor(images=image, return_tensors="pt")
        
        # Generate caption
        caption = model.generate(**inputs)
        caption_text = processor.decode(caption[0], skip_special_tokens=True)
        
        # Display the caption
        st.write(f"Caption: **{caption_text}**")


# %%


# %%




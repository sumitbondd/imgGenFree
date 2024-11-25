import streamlit as st
from PIL import Image
import io
from utils import query_hf_api

# Streamlit UI
st.title("🖌️ AI Image Generator")
st.subheader("Generate images from text prompts using Stable Diffusion!")

# Input prompt
prompt = st.text_input("Enter your image prompt:", "")

# Generate button
if st.button("Generate Image"):
    if prompt.strip():
        with st.spinner("Generating image... Please wait."):
            try:
                # Query the Hugging Face API
                image_bytes = query_hf_api(prompt)
                image = Image.open(io.BytesIO(image_bytes))
                
                # Display the generated image
                st.image(image, caption="Generated Image", use_container_width=True)  # Updated here
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.error("Please enter a prompt to generate an image.")

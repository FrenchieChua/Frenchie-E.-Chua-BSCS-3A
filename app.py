import streamlit as st
import openai
import requests
from requests.structures import CaseInsensitiveDict

# Set up the OpenAI API
openai.api_key = st.secrets["api_key"]

# Define a function to generate images from text
def generate_image(prompt):
    data = """
    {
        """
    data += f'"model": "image-alpha-001",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"512x512",
        "response_format":"url"
    }
    """
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = f"Bearer {openai.api_key}"
    resp = requests.post("https://api.openai.com/v1/images/generations", headers=headers, data=data)

    if resp.status_code != 200:
        raise ValueError("Failed to generate image")

    response_text = resp.text.replace('"', '')
    return response_text

# Define some sample prompts
prompts = [
    "A visualization of the solar system",
    "A diagram of the human brain",
    "A representation of the water cycle",
    "An illustration of the process of photosynthesis",
    "A map of the world with countries labeled"
]

# Define the Streamlit app
st.title("Visual Tutor")

# Display the sample prompts
st.write("Choose a prompt or enter your own:")
prompt = st.selectbox("Prompt", prompts, index=0)
if prompt == "Enter your own":
    prompt = st.text_input("Enter a prompt", "")

# Generate and display the image
if prompt:
    st.write("Generating image...")
    image_url = generate_image(prompt)
    st.image(image_url)

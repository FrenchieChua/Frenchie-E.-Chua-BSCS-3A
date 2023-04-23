import streamlit as st
import openai
import json
import requests

openai.api_key = "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"


# Load categories from text file
url_categories = 'https://raw.githubusercontent.com/FrenchieChuaFrenchie-E.-Chua-BSCS3A/Main/categories.txt'
categories = requests.get(url_categories).text.splitlines()

# Define function to classify an object using ChatGPT
def classify_object(object_name):
    # Prompt ChatGPT to classify the object
    prompt = f"Please classify the object '{object_name}' into one of the following categories: {', '.join(categories)}."
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the classification from the API response
    classification = response.choices[0].text.strip()

    # Return the classification
    return classification

# Define function to classify multiple objects
def classify_objects(object_list):
    # Classify each object and store the results in a dictionary
    classifications = {}
    for object_name in object_list:
        classification = classify_object(object_name)
        classifications[object_name] = classification

    # Return the dictionary of classifications
    return classifications

# Load objects from text file
url_objects = 'https://raw.githubusercontent.com/FrenchieChuaFrenchie-E.-Chua-BSCS3A/Main/tobjects.txt'
objects = requests.get(url_objects).text.splitlines()

# Classify the objects
classifications = classify_objects(objects)

# Print the results
for object_name, classification in classifications.items():
    st.write(f"The object '{object_name}' was classified as '{classification}'.")

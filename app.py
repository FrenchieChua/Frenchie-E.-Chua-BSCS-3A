import streamlit as st
import openai
import json


openai.api_key = "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"

# Load categories from text file
with open("categories.txt", "r") as f:
    categories = [line.strip() for line in f.readlines()]
    
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
with open("objects.txt", "r") as f:
    objects = [line.strip() for line in f.readlines()]
    
# Classify the objects
classifications = classify_objects(objects)

# Print the results
for object_name, classification in classifications.items():
    st.write(f"The object '{object_name}' was classified as '{classification}'.")

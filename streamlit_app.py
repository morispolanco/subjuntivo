import streamlit as st
import spacy

# Load the Spanish language model
nlp = spacy.load("es_core_news_sm")

# Define the function to extract verbs in subjunctive mode
def extract_subjunctive_verbs(text):
    doc = nlp(text)
    verbs = []
    for token in doc:
        if token.pos_ == "VERB" and token.tag_.startswith("V"):
            verbs.append(token.text)
    return verbs

# Create the Streamlit app
st.title("Spanish Subjunctive Verb Extractor")

# Get the input text from the user
text = st.text_input("Enter a Spanish text:")

# Extract the verbs in subjunctive mode
subjunctive_verbs = extract_subjunctive_verbs(text)

# Display the extracted verbs
if subjunctive_verbs:
    st.write("Subjunctive verbs in the text:")
    st.write(subjunctive_verbs)
else:
    st.write("No subjunctive verbs found in the text.")

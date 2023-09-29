import spacy
from spacy.lang.es import Spanish


# Load the Spanish language model
nlp = Spanish()


# Define a function to extract verbs in subjunctive mode
def extract_subjunctive_verbs(text):
    doc = nlp(text)
    subjunctive_verbs = []
    for token in doc:
        if token.tag_ == "VMIS":
            subjunctive_verbs.append(token.text)
    return subjunctive_verbs


# Define a Streamlit app to interact with the user
import streamlit as st

st.title("Verb Extractor")
st.write("This app extracts verbs in subjunctive mode from Spanish texts.")


text = st.text_area("Enter the text to analyze:")


if text:
    subjunctive_verbs = extract_subjunctive_verbs(text)
    if subjunctive_verbs:
        st.write("Subjunctive verbs in the text:")
        for verb in subjunctive_verbs:
            st.write(verb)
    else:
        st.write("No subjunctive verbs found.")

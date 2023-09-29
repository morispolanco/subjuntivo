import spacy
import streamlit as st


# Load the Spanish model
nlp = spacy.load("es_core_news_sm")


# Define a function to extract subjunctive verbs
def extract_subjunctive_verbs(text):
    doc = nlp(text)
    subjunctive_verbs = []
    for token in doc:
        if token.pos_ == "VERB" and token.tag_ == "VMIS":
            subjunctive_verbs.append(token.text)
    return subjunctive_verbs


# Create a Streamlit app
st.title("Subjunctive Verb Extractor")
st.markdown("Enter a text in Spanish:")
text = st.text_area(label="Text", value="", height=20)


if text:
    subj_verbs = extract_subjunctive_verbs(text)
    if subj_verbs:
        st.write("Subjunctive verbs found:")
        for verb in subj_verbs:
            st.write(verb)
    else:
        st.write("No subjunctive verbs found.")

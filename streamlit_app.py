import streamlit as st
import spacy
from spacy_conjugator import SpacyConjugator

@st.cache(allow_output_mutation=True) 
def load_model():
    nlp = spacy.load("es_core_news_md")
    conjugator = SpacyConjugator(nlp)
    return nlp, conjugator

nlp, conjugator = load_model() 

st.title("Find Verbs in Subjunctive Mode")

text = st.text_area("Enter Text in Spanish", "Ella quiso que yo viniera a la fiesta.")

if text:
    doc = nlp(text)
    verbs = []
    for token in doc:
        if token.pos_ == "VERB" and conjugator.conjugate(token, tense="present", mood="subjunctive"):
            verbs.append(token.text)
    
    if verbs:
        st.write("Verbs in subjunctive mode found:", ", ".join(verbs))
    else:
        st.write("No verbs in subjunctive mode found.")

import streamlit as st
import spacy
from spacy.lang.es import Spanish

nlp = spacy.load('es_core_news_sm')

def extract_subjunctive_verbs(text):
    doc = nlp(text)
    subjunctive_verbs = [token.text for token in doc if token.tag_ == "VERB" and token.morph.get("Mood") == ["Subj"]]
    return subjunctive_verbs

st.title('Spanish Subjunctive Verb Extractor')

input_text = st.text_area("Enter Spanish text here")

if st.button('Extract Subjunctive Verbs'):
    result = extract_subjunctive_verbs(input_text)
    st.write(result)

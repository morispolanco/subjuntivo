import streamlit as st
import spacy

nlp = spacy.load("es_core_news_sm")

def get_verbs(text):
    doc = nlp(text)
    verbs = [token.lemma_ for token in doc if token.pos_ == "VERB" and token.tag_ == "VS"]
    return verbs

st.title("Subjunctive Verbs Extractor")
text = st.text_area("Enter Spanish text:", value="Estoy cansado de trabajar todos los días.")
verbs = get_verbs(text)
st.write("Subjunctive verbs:", verbs)

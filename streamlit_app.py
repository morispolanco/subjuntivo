import streamlit as st
import spacy
from spacy import displacy

# Carga el modelo de lenguaje de spaCy para español
nlp = spacy.load("es_core_news_sm")

# Define una función que extraiga los verbos en subjuntivo de un texto
def extract_subjunctive_verbs(text):
    doc = nlp(text)
    verbs = []
    for token in doc:
        if token.pos_ == "VERB" and token.mood == "SUBJ":
            verbs.append(token.text)
    return verbs

# Crea una interfaz de usuario con Streamlit para que el usuario pueda ingresar el texto y ver los verbos en subjuntivo
st.title("Extractor de verbos en subjuntivo")
text = st.text_input("Ingrese el texto:")
if st.button("Extraer verbos en subjuntivo"):
    verbs = extract_subjunctive_verbs(text)
    st.write("Verbos en subjuntivo:")
    st.write(verbs)

import streamlit as st
import spacy
from spacy import displacy

# Cargar el modelo de lenguaje de spaCy para español
nlp = spacy.load("es_core_news_sm")

# Definir una función que tome un texto como entrada y devuelva una lista de verbos en modo subjuntivo
def find_subjunctive_verbs(text):
    doc = nlp(text)
    verbs = []
    for token in doc:
        if token.pos_ == "VERB" and token.mood == "SUBJ":
            verbs.append(token.text)
    return verbs

# Crear una interfaz de usuario con Streamlit para que el usuario pueda ingresar el texto y ver los verbos en modo subjuntivo
st.title("Verbos en modo subjuntivo")
text = st.text_input("Ingrese el texto:")
verbs = find_subjunctive_verbs(text)
st.write("Verbos en modo subjuntivo:")
st.write(verbs)

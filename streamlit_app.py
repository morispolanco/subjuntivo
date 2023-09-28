import streamlit as st
import spacy
from spacy import attrs

# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_sm")

# Función para obtener los verbos en subjuntivo
def obtener_verbos_subjuntivo(texto):
    # Procesar el texto con spaCy
    doc = nlp(texto)
    
    # Obtener los verbos en subjuntivo
    verbos_subjuntivo = []
    for token in doc:
        if token.pos_ == "VERB" and "Mood=Sub" in token.morph.get(attrs.MORPH):
            verbos_subjuntivo.append(token.text)
    
    return verbos_subjuntivo

# Configurar la interfaz de la aplicación
st.title("Verbos en Subjuntivo")
texto = st.text_input("Ingrese un texto:")
if texto:
    verbos_subjuntivo = obtener_verbos_subjuntivo(texto)
    st.write("Verbos en subjuntivo:")
    for verbo in verbos_subjuntivo:
        st.write(verbo)

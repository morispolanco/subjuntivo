import spacy
import streamlit as st

# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_sm")

# Función para obtener los verbos en subjuntivo
def obtener_verbos_subjuntivo(texto):
    # Procesar el texto con spaCy
    doc = nlp(texto)
    
    # Obtener los verbos en subjuntivo
    verbos_subjuntivo = [token.text for token in doc if token.pos_ == "VERB" and token.dep_ == "subj"]
    
    return verbos_subjuntivo

# Configurar la interfaz de la aplicación
st.title("Verbos en Subjuntivo")
texto = st.text_input("Ingrese un texto:")
if texto:
    verbos_subjuntivo = obtener_verbos_subjuntivo(texto)
    st.write("Verbos en subjuntivo:")
    for verbo in verbos_subjuntivo:
        st.write(verbo)

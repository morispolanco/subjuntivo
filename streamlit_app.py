import streamlit as st
import spacy
from spacy.matcher import Matcher

# Cargar el modelo de spaCy
nlp = spacy.load("es_core_news_sm")

# Definir la regla para identificar los verbos en subjuntivo
matcher = Matcher(nlp.vocab)
pattern = [{"POS": "VERB"}, {"Mood": "Sub"}]
matcher.add("VERB_SUBJ", None, pattern)

# Función para obtener los verbos en subjuntivo
def obtener_verbos_subjuntivo(texto):
    # Procesar el texto con spaCy
    doc = nlp(texto)
    
    # Buscar los verbos en subjuntivo utilizando la regla personalizada
    matches = matcher(doc)
    
    # Obtener los verbos en subjuntivo
    verbos_subjuntivo = [doc[start:end].text for _, start, end in matches]
    
    return verbos_subjuntivo

# Configurar la interfaz de la aplicación
st.title("Verbos en Subjuntivo")
texto = st.text_input("Ingrese un texto:")
if texto:
    verbos_subjuntivo = obtener_verbos_subjuntivo(texto)
    st.write("Verbos en subjuntivo:")
    for verbo in verbos_subjuntivo:
        st.write(verbo)

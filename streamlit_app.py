import streamlit as st
import spacy

# Cargar el modelo de Spacy para español
nlp = spacy.load("es_core_news_sm")

# Título de la aplicación
st.title("Extracción de verbos en subjuntivo en español")

# Texto de entrada
text = st.text_area("Ingrese el texto en español:", height=200)

# Botón para extraer los verbos en subjuntivo
if st.button("Extraer verbos en subjuntivo"):
    # Procesar el texto con Spacy
    doc = nlp(text)

    # Encontrar los verbos en subjuntivo en el texto
    verbos_subjuntivo = [token.text for token in doc if token.pos_ == "VERB" and token.mood == "SUBJ"]

    # Mostrar los verbos en subjuntivo encontrados
    st.subheader("Verbos en subjuntivo encontrados:")
    for verbo in verbos_subjuntivo:
        st.write(verbo)

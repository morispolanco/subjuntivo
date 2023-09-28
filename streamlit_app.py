import streamlit as st
import spacy

# Cargar el modelo de Spacy para español
nlp = spacy.load("es_core_news_sm")

# Título de la aplicación
st.title("Localizador de verbos en subjuntivo")

# Texto de entrada
text = st.text_area("Ingrese el texto en español:", height=200)

# Botón para analizar el texto
if st.button("Analizar"):
    # Procesar el texto con Spacy
    doc = nlp(text)

    # Encontrar los verbos en subjuntivo
    subjunctive_verbs = [token.text for token in doc if token.pos_ == "VERB" and token.mood == "SUBJ"]

    # Mostrar los resultados
    if subjunctive_verbs:
        st.success("Se encontraron los siguientes verbos en subjuntivo:")
        for verb in subjunctive_verbs:
            st.write(verb)
    else:
        st.info("No se encontraron verbos en subjuntivo en el texto.")

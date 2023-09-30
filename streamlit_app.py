import streamlit as st
import spacy

# Cargar el modelo de lenguaje
nlp = spacy.load("es_core_news_sm")

# Definir una función para encontrar verbos en subjuntivo
def find_subjunctive_verbs(text):
    doc = nlp(text)
    subjunctive_verbs = []
    for token in doc:
        if token.pos_ == "VERB" and token.tag_ == "SUBJ":
            subjunctive_verbs.append(token.text)
    return subjunctive_verbs

def main():
    st.title("Extracción de Verbos en Subjuntivo")
    text = st.text_area("Ingrese un texto en español:")
    
    if st.button("Buscar Verbos en Subjuntivo"):
        subjunctive_verbs = find_subjunctive_verbs(text)
        st.write("Verbos en Subjuntivo encontrados:")
        for verb in subjunctive_verbs:
            st.write(verb)

if __name__ == "__main__":
    main()

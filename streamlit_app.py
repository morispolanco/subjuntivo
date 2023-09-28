import streamlit as st
import spacy

def buscar_subjuntivos(texto):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    subjuntivos = [token.text for token in doc if token.pos_ == "VERB" and token.mood == "SUBJUNCTIVE"]
    return subjuntivos

def main():
    st.title("Aplicación de búsqueda de subjuntivos")
    st.write("Ingrese un texto para buscar subjuntivos")

    texto = st.text_area("Texto")

    if st.button("Buscar"):
        subjuntivos = buscar_subjuntivos(texto)
        if subjuntivos:
            st.write("Subjuntivos encontrados:")
            for subjuntivo in subjuntivos:
                st.write(subjuntivo)
        else:
            st.write("No se encontraron subjuntivos en el texto")

if __name__ == "__main__":
    main()

import streamlit as st
import spacy

def extraer_subjuntivos(texto):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    subjuntivos = [token.text for token in doc if token.pos_ == "VERB" and token.mood == "SUBJ"]
    return subjuntivos

def main():
    st.title("Extracción de Subjuntivos en un Texto")
    st.write("Esta aplicación utiliza Spacy y el modelo es_core_news_sm para extraer los subjuntivos en un texto en español.")

    texto = st.text_area("Ingrese un texto:")
    
    if st.button("Extraer Subjuntivos"):
        subjuntivos = extraer_subjuntivos(texto)
        st.write("Subjuntivos encontrados:")
        for subjuntivo in subjuntivos:
            st.write(subjuntivo)

if __name__ == "__main__":
    main()

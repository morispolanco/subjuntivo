import streamlit as st
import spacy

def encontrar_verbos_subjuntivo(texto):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    verbos_subjuntivo = []
    for token in doc:
        if token.pos_ == "VERB" and "Sub" in token.morph.get("Mood", []):
            verbos_subjuntivo.append(token.text)
    return verbos_subjuntivo

def main():
    st.title("Buscador de Verbos en Modo Subjuntivo")
    texto = st.text_area("Ingresa el texto:")
    if st.button("Buscar verbos en modo subjuntivo"):
        verbos_subjuntivo = encontrar_verbos_subjuntivo(texto)
        st.write("Verbos en modo subjuntivo encontrados:")
        for verbo in verbos_subjuntivo:
            st.write(verbo)

if __name__ == "__main__":
    main()

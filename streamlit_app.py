import streamlit as st
import spacy

def cambiar_conjugaciones(texto):
    nlp = spacy.load("es_core_news_sm", disable=["parser", "ner"])
    doc = nlp(texto)
    resultado = []
    for token in doc:
        if token.tag_ == "PRON__Per=1|Num=Sing":
            resultado.append(token.lemma_ + "a")
        else:
            resultado.append(token.text)
    return " ".join(resultado)

def main():
    st.title("Cambiador de Conjugaciones")
    texto = st.text_area("Ingresa el texto semiespañol:")
    if st.button("Cambiar conjugaciones"):
        resultado = cambiar_conjugaciones(texto)
        st.write("Texto corregido:")
        st.write(resultado)

if __name__ == "__main__":
    main()

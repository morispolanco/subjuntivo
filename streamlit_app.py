import streamlit as st
import spacy

def analyze_text(text):
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(text)
    subjunctive_count = 0
    for token in doc:
        if token.tag_ == 'SP':
            subjunctive_count += 1
    return subjunctive_count

def main():
    st.title("Análisis de Modo Subjuntivo")
    text = st.text_area("Ingrese el texto a analizar", "")
    if st.button("Analizar"):
        subjunctive_count = analyze_text(text)
        st.write(f"El texto contiene {subjunctive_count} ocurrencias del modo subjuntivo.")

if __name__ == "__main__":
    main()

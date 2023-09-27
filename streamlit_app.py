import streamlit as st
import spacy
from spacy import displacy
from spacy.lang.es import Spanish

def main():
    st.title("Análisis Gramatical de Textos en Español")
    text = st.text_area("Ingrese el texto a analizar", "")
    if st.button("Analizar"):
        analyze_text(text)

def analyze_text(text):
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(text)
    for sent in doc.sents:
        displacy.render(sent, style='dep', options={'compact': True, 'distance': 100})

if __name__ == "__main__":
    main()

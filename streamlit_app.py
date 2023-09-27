import streamlit as st
import spacy
from spacy import displacy
from spacy.lang.es import Spanish
import PyPDF2
from transformers import pipeline

def main():
    st.title("Análisis Gramatical y Preguntas sobre Textos en Español")
    option = st.selectbox("Seleccione una opción", ("Cargar archivo PDF", "Ingresar texto manualmente"))
    
    if option == "Cargar archivo PDF":
        pdf_file = st.file_uploader("Cargar archivo PDF", type="pdf")
        if pdf_file is not None:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ""
            for page in range(pdf_reader.numPages):
                text += pdf_reader.getPage(page).extractText()
            analyze_text(text)
            question = st.text_input("Ingrese una pregunta sobre el texto", "")
            if st.button("Responder"):
                answer_question(text, question)
    
    elif option == "Ingresar texto manualmente":
        text = st.text_area("Ingrese el texto a analizar", "")
        if st.button("Analizar"):
            analyze_text(text)
            question = st.text_input("Ingrese una pregunta sobre el texto", "")
            if st.button("Responder"):
                answer_question(text, question)

def analyze_text(text):
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(text)
    for sent in doc.sents:
        displacy.render(sent, style='dep', options={'compact': True, 'distance': 100})

def answer_question(text, question):
    nlp = pipeline("question-answering", model="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es", tokenizer="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es")
    result = nlp(question=question, context=text)
    st.write("Pregunta:", question)
    st.write("Respuesta:", result["answer"])

if __name__ == "__main__":
    main()

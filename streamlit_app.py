import streamlit as st
import subprocess
import PyPDF2
import spacy
from spacy import displacy
from spacy.lang.es import Spanish
from transformers import pipeline

def download_model():
    command = ["python", "-m", "spacy", "download", "es_core_news_sm"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        st.success("El modelo se ha descargado correctamente")
    else:
        st.error(f"Error al descargar el modelo: {stderr.decode('utf-8')}")

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
    # Descargar el modelo de lenguaje spaCy al iniciar la aplicación
    download_model()
    main()

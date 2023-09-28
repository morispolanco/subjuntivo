import streamlit as st
import subprocess
import spacy

def descargar_modelo():
    comando = "python -m spacy download es_core_news_sm"
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate()
    
    if proceso.returncode == 0:
        st.write("Modelo descargado correctamente.")
    else:
        st.write("Error al descargar el modelo:", error.decode())

# Llamar a la función para descargar el modelo
descargar_modelo()

# Cargar el modelo de spaCy
nlp = spacy.load('es_core_news_sm')

# Aplicación Streamlit
st.title("Aplicación de procesamiento de texto")

texto = st.text_area("Ingrese un texto en español", "")

if st.button("Procesar"):
    doc = nlp(texto)
    subjuntivos = [token.text for token in doc if token.pos_ == "VERB" and token.morph.get("Mood") == "Sub"]
    
    if subjuntivos:
        st.write("Verbos en modo subjuntivo encontrados:")
        for verbo in subjuntivos:
            st.write(verbo)
    else:
        st.write("No se encontraron verbos en modo subjuntivo en el texto.")

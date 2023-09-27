import streamlit as st
import subprocess

def descargar_modelo():
    comando = "python -m spacy download es_core_news_sm"
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate()
    if proceso.returncode == 0:
        st.write("El modelo se ha descargado correctamente.")
    else:
        st.error(f"Error al descargar el modelo: {error.decode()}")

def main():
    st.title("Descargar modelo de spaCy")
    st.write("Presiona el botón para descargar el modelo de lenguaje.")
    if st.button("Descargar modelo"):
        descargar_modelo()

if __name__ == "__main__":
    main()

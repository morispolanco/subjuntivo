import streamlit as st
import subprocess

def descargar_modelo():
    comando = "python -m spacy download es_core_news_sm"
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate()
    if proceso.returncode == 0:
        st.write("El modelo se ha descargado correctamente."import streamlit as st
import spacy.cli

def descargar_modelo():
    spacy.cli.download("es_core_news_sm")
    st.write("El modelo se ha descargado correctamente.")

def cambiar_conjugaciones(texto):
    nlp = spacy.load("es_core_news_sm")
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
    if st.button("Descargar modelo"):
        descargar_modelo()
    if st.button("Cambiar conjugaciones"):
        resultado = cambiar_conjugaciones(texto)
        st.write("Texto corregido:")
        st.write(resultado)

if __name__ == "__main__":
    main())
    else:
        st.error(f"Error al descargar el modelo: {error.decode()}")

def main():
    st.title("Descargar modelo de spaCy")
    st.write("Presiona el botón para descargar el modelo de lenguaje.")
    if st.button("Descargar modelo"):
        descargar_modelo()

if __name__ == "__main__":
    main()

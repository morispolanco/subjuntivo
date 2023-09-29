import streamlit as st
from spacy import displacy

import spacy

nlp = spacy.download("es_core_news_sm")

# Definir la función para buscar subjuntivos
def buscar_subjuntivos(texto):
    # Crear un objeto de spaCy para el texto
    doc = nlp(texto)
    # Buscar los tokens que son subjuntivos
    subjuntivos = [token for token in doc if token.dep_ == "subj"]
    # Devolver una lista con los subjuntivos encontrados
    return subjuntivos

# Definir la función para mostrar los subjuntivos en la interfaz de Streamlit
def mostrar_subjuntivos(subjuntivos):
    # Crear una tabla para mostrar los subjuntivos
    table = st.table(subjuntivos)
    # Mostrar la tabla en la interfaz de Streamlit
    st.write(table)

# Definir la función principal de la aplicación
def main():
    # Crear un objeto de Streamlit para la interfaz de usuario
    st.title("Buscador de subjuntivos")
    # Crear un campo de texto para ingresar el texto a analizar
    texto = st.text_input("Ingrese el texto a analizar:")
    # Crear un botón para ejecutar la función de buscar subjuntivos
    st.button("Buscar subjuntivos", on_click=buscar_subjuntivos(texto))
    # Mostrar los subjuntivos encontrados en la interfaz de Streamlit
    mostrar_subjuntivos(buscar_subjuntivos(texto))

# Ejecutar la función principal de la aplicación
if __name__ == "__main__":
    main()

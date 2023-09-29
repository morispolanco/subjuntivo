import streamlit as st
import spacy

def extraer_verbos_subjuntivo(texto):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    
    verbos_subjuntivo = []
    
    for token in doc:
        if token.pos_ == "VERB" and token.morph.get("Mood") == "Sub":
            verbos_subjuntivo.append(token.text)
    
    return verbos_subjuntivo

# Configuración de la página
st.set_page_config(page_title="Extracción Verbos Subjuntivo", layout="wide")

# Título y descripción
st.title("Extracción Verbos Subjuntivo")
st.write("Esta aplicación extrae los verbos en subjuntivo presentes en un texto.")

# Textarea para ingresar el texto
texto_input = st.text_area(label="Ingrese su texto aquí", height=200)

if st.button("Extraer"):
    # Verificar si se ingresó algún texto antes de procesar
    if not texto_input:
        st.warning("Por favor, ingrese un texto.")
    else:
        # Llamar a la función para extraer los verbos en subjuntivo y mostrarlos al usuario
        lista_verbos_subj = extraer_verbos_subjuntivo(texto_input)
        
        if len(lista_verbos_subj) > 0:
            st.success(f"Se encontraron {len(lista_verbos_subj)} verbos en subjuntivo:")
            for verbo in lista_verbos_subj:
                st.write(verbo)
        else:
            st.warning("No se encontraron verbos en subjuntivo en el texto ingresado.")

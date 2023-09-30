import streamlit as st
import spacy

def extract_subjunctive_verbs(text):
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(text)
    
    subjunctive_verbs = []
    
    for token in doc:
        if token.pos_ == 'VERB' and token.mood == 'SUBJ':
            subjunctive_verbs.append(token.text)
            
    return subjunctive_verbs


# Configuración de la página
st.set_page_config(page_title="Extracción de Verbos en Subjuntivo", layout="wide")

# Título y descripción de la aplicación
st.title("Extracción de Verbos en Subjuntivo")
st.markdown("""
Esta aplicación extrae los verbos en subjuntivo presentes en un texto escrito 
en español utilizando la biblioteca spaCy.
""")

# Área para ingresar el texto
text_input = st.text_area("Ingrese el texto:", height=200)

if st.button("Extraer"):
    if len(text_input.strip()) > 0:
        verbs = extract_subjunctive_verbs(text_input)
        
        if len(verbs) > 0:
            # Mostrar los verbos encontrados
            st.success(f"Se encontraron {len(verbs)} verbos en subjuntivo:")
            for i, verb in enumerate(verbs):
                st.write(f"{i+1}. {verb}")
        else:
            # Si no se encontraron verbos, mostrar mensaje informativo
            st.info("No se encontraron verbos en subjuntivo.")

import streamlit as st
import pandas as pd
import docx2txt
import re

# Título de la aplicación
st.title("Extracción de oraciones con expresiones de deseo")

# Campo de carga de archivo .docx
uploaded_file = st.file_uploader("Cargar archivo .docx", type="docx")

# Lista de expresiones de deseo en español
expresiones = ["quiero que", "espero que", "ojalá que", "deseo que",
               "espero que", "deseo que", "ojalá que", "quisiera que",
               "me gustaría que", "sería bueno que", "sería genial que",
               "sería fantástico que", "sería maravilloso que",
               "sería increíble que", "sería ideal que", "sería perfecto que",
               "sería estupendo que", "sería fabuloso que", "sería deseable que"]

# Función para extraer las oraciones con expresiones de deseo
def extraer_oraciones(texto):
    # Patrón regex para buscar las oraciones con expresiones de deseo
    patron = r"(?i)([^.!?]*(" + "|".join(expresiones) + r")[^.!?]*)[.!?]"
    
    # Buscar coincidencias en el texto
    coincidencias = re.findall(patron, texto)
    
    # Crear una lista con las oraciones
    oraciones = [coincidencia[0] for coincidencia in coincidencias]
    
    return oraciones

# Botón para extraer las oraciones
if st.button("Extraer oraciones"):
    if uploaded_file is not None:
        texto_docx = docx2txt.process(uploaded_file)
        oraciones = extraer_oraciones(texto_docx)
        
        if oraciones:
            st.success("Se han extraído las oraciones exitosamente.")
            st.markdown("### Resultado")
            for oracion in oraciones:
                st.write("- " + oracion)
        else:
            st.warning("No se encontraron oraciones con expresiones de deseo.")
    else:
        st.warning("Por favor, carga un archivo .docx.")

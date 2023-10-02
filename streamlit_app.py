import streamlit as st
import pandas as pd
import docx2txt
import re
import base64

# Título de la aplicación
st.title("Extracción de expresiones de deseo y palabras siguientes")

# Campo de carga de archivo .docx
uploaded_file = st.file_uploader("Cargar archivo .docx", type="docx")

# Lista de expresiones de deseo en español
expresiones = ["quiero que", "espero que", "ojalá que", "deseo que",
               "espero que", "deseo que", "ojalá que", "quisiera que",
               "me gustaría que", "sería bueno que", "sería genial que",
               "sería fantástico que", "sería maravilloso que",
               "sería increíble que", "sería ideal que", "sería perfecto que",
               "sería estupendo que", "sería fabuloso que", "sería deseable que"]

# Función para extraer las expresiones de deseo y las dos palabras siguientes
def extraer_expresiones(texto):
    # Patrón regex para buscar las expresiones de deseo y las dos palabras siguientes
    patron = r"(?i)(" + "|".join(expresiones) + r")\s+(\w+)\s+(\w+)"
    
    # Buscar coincidencias en el texto
    coincidencias = re.findall(patron, texto)
    
    # Crear un DataFrame con las expresiones de deseo y las palabras siguientes
    df = pd.DataFrame(coincidencias, columns=["Expresión", "Palabra 1", "Palabra 2"])
    
    return df

# Botón para extraer las expresiones y palabras y descargar el archivo CSV
if st.button("Extraer expresiones y palabras"):
    if uploaded_file is not None:
        texto_docx = docx2txt.process(uploaded_file)
        df_expresiones = extraer_expresiones(texto_docx)
        
        if not df_expresiones.empty:
            st.success("Se han extraído las expresiones y palabras exitosamente.")
            st.markdown("### Resultado")
            st.table(df_expresiones)
            
            st.markdown("### Descargar archivo CSV")
            csv = df_expresiones.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="expresiones.csv">Descargar CSV</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("No se encontraron expresiones de deseo y palabras siguientes.")
    else:
        st.warning("Por favor, carga un archivo .docx.")

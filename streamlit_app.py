import streamlit as st
import pandas as pd
import docx2txt
import re
import base64

# Título de la aplicación
st.title("Extracción de verbos después de expresiones de esperanza o deseo")

# Campo de carga de archivo .docx
uploaded_file = st.file_uploader("Cargar archivo .docx", type="docx")

# Función para extraer los verbos después de expresiones de esperanza o deseo
def extraer_verbos(texto):
    # Expresiones de esperanza o deseo en español
    expresiones = ["quiero que", "espero que", "ojalá que", "deseo que"]
    
    # Patrón regex para buscar las expresiones seguidas de un verbo
    patron = r"(?i)(" + "|".join(expresiones) + r")\s+(\w+)"
    
    # Buscar coincidencias en el texto
    coincidencias = re.findall(patron, texto)
    
    # Crear un DataFrame con los verbos y su frecuencia
    df = pd.DataFrame(coincidencias, columns=["Expresión", "Verbo"])
    df["Frecuencia"] = df.groupby("Verbo")["Verbo"].transform("count")
    df = df.drop_duplicates().reset_index(drop=True)
    
    return df

# Botón para extraer los verbos y descargar el archivo CSV
if st.button("Extraer verbos"):
    if uploaded_file is not None:
        texto_docx = docx2txt.process(uploaded_file)
        df_verbos = extraer_verbos(texto_docx)
        
        if not df_verbos.empty:
            st.success("Se han extraído los verbos exitosamente.")
            st.markdown("### Resultado")
            st.dataframe(df_verbos)
            
            st.markdown("### Descargar archivo CSV")
            csv = df_verbos.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="verbos.csv">Descargar CSV</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("No se encontraron verbos después de las expresiones de esperanza o deseo.")
    else:
        st.warning("Por favor, carga un archivo .docx.")

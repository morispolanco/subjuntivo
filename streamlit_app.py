import streamlit as st
import tabula
import pandas as pd
import base64

# Título de la aplicación
st.title("Conversión de PDF a CSV")

# Campo de carga de archivo PDF
uploaded_file = st.file_uploader("Cargar archivo PDF", type="pdf")

# Función para convertir el PDF a CSV
def convert_to_csv(pdf_file):
    # Leer el archivo PDF y extraer las tablas
    tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
    
    # Concatenar todas las tablas en un solo DataFrame
    df = pd.concat(tables)
    
    # Guardar el DataFrame en un archivo CSV
    csv_file = "output.csv"
    df.to_csv(csv_file, index=False)
    
    return csv_file

# Botón para convertir el PDF a CSV y descargar el archivo
if st.button("Convertir a CSV"):
    if uploaded_file is not None:
        csv_file = convert_to_csv(uploaded_file)
        st.success("El archivo se ha convertido exitosamente a CSV.")
        st.markdown("### Descargar archivo CSV")
        with open(csv_file, "rb") as file:
            b64 = base64.b64encode(file.read()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="output.csv">Descargar CSV</a>'
            st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("Por favor, cargue un archivo PDF.")

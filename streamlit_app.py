import streamlit as st
import re
import pandas as pd
import base64

# Título de la aplicación
st.title("Extracción de verbos después de expresiones de deseo o esperanza")

# Campo de carga de archivo de texto
uploaded_file = st.file_uploader("Cargar archivo de texto", type="txt")

# Expresiones de deseo o esperanza
expressions = ["quiero que", "espero que", "deseo que", "ojalá que"]

# Función para extraer los verbos después de las expresiones
def extract_verbs(text):
    verbs = []
    sentences = re.split(r"[.!?]", text)
    for sentence in sentences:
        for expression in expressions:
            if expression in sentence:
                verb_match = re.search(re.escape(expression) + r"\s+(\w+)", sentence)
                if verb_match:
                    verbs.append(verb_match.group(1))
    return verbs

# Botón para extraer los verbos y guardar en un archivo CSV
if st.button("Extraer verbos y guardar en CSV"):
    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        extracted_verbs = extract_verbs(text)
        if extracted_verbs:
            verb_freq = pd.Series(extracted_verbs).value_counts().reset_index()
            verb_freq.columns = ['Verbo', 'Frecuencia']
            st.success("Los verbos extraídos son:")
            st.write(verb_freq)
            st.markdown("### Descargar archivo CSV")
            csv = verb_freq.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="verbos.csv">Descargar CSV</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("No se encontraron verbos después de las expresiones de deseo o esperanza.")
    else:
        st.warning("Por favor, cargue un archivo de texto.")

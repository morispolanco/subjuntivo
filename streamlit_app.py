import re
import streamlit as st

def identificar_verbos_subjuntivos(texto):
    # Definir el patrón para la conjugación verbal en subjuntivo
    patron = r"\b(?P<verbo>[a-zA-Zá-úÁ-ÚñÑ]+[aei]s{0,1}a{0,1}r{0,1})\b"

    # Encontrar todas las coincidencias del patrón en el texto
    coincidencias = re.findall(patron, texto)

    # Filtrar las coincidencias que no son verbos (por ejemplo, "que")
    verbos_subjuntivos = [coincidencia for coincidencia in coincidencias if coincidencia.lower() != "que"]

    return verbos_subjuntivos

# Título de la aplicación
st.title("Identificador de Verbos en Subjuntivo")

# Ingresar el texto
texto = st.text_area("Ingrese el texto")

# Botón para identificar los verbos en subjuntivo
if st.button("Identificar"):
    if texto:
        verbos_subjuntivos = identificar_verbos_subjuntivos(texto)
        st.write("Verbos en subjuntivo encontrados:")
        for verbo in verbos_subjuntivos:
            st.write(verbo)
    else:
        st.warning("Por favor, ingrese un texto antes de identificar los verbos en subjuntivo.")

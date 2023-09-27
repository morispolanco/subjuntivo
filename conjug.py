import streamlit as st
from pattern.es import conjugate, INFINITIVE

def cambiar_conjugaciones(texto):
    palabras = texto.split()
    resultado = []
    for palabra in palabras:
        if palabra.endswith("o"):
            verbo_infinitivo = palabra[:-1] + "ar"  # Suponiendo que los verbos son regulares y terminan en "ar"
            verbo_tercera_persona = conjugate(verbo_infinitivo, person=3, tense=INFINITIVE)
            resultado.append(verbo_tercera_persona)
        else:
            resultado.append(palabra)
    return " ".join(resultado)

def main():
    st.title("Cambiador de Conjugaciones")
    texto = st.text_area("Ingresa el texto semiespañol:")
    if st.button("Cambiar conjugaciones"):
        resultado = cambiar_conjugaciones(texto)
        st.write("Texto corregido:")
        st.write(resultado)

if __name__ == "__main__":
    main()

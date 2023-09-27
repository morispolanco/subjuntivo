import streamlit as st
from pattern.es import parse, split

def encontrar_verbos_subjuntivo(texto):
    parsed_text = parse(texto, lemmata=True).split()
    verbos_subjuntivo = []
    for sentence in parsed_text:
        for word, tag, _, _ in sentence:
            if "SUBJ" in tag:
                verbos_subjuntivo.append(word)
    return verbos_subjuntivo

def main():
    st.title("Buscador de Verbos en Modo Subjuntivo")
    texto = st.text_area("Ingresa el texto:")
    if st.button("Buscar verbos en modo subjuntivo"):
        verbos_subjuntivo = encontrar_verbos_subjuntivo(texto)
        if verbos_subjuntivo:
            st.write("Verbos en modo subjuntivo encontrados:")
            for verbo in verbos_subjuntivo:
                st.write(verbo)
        else:
            st.write("No se encontraron verbos en modo subjuntivo.")

if __name__ == "__main__":
    main()

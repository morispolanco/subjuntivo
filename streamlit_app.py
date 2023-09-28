
import streamlit as st
import spacy
import csv

def encontrar_verbos_subjuntivo(texto):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(texto)
    verbos_subjuntivo = []
    for token in doc:
        if token.pos_ == "VERB" and "Sub" in token.morph.get("Mood", ""):
            verbos_subjuntivo.append(token.text)
    return verbos_subjuntivo

def exportar_a_csv(verbos_subjuntivo):
    with open("resultados.csv", "w", newline="") as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Verbo", "Frecuencia"])
        frecuencias = {}
        for verbo in verbos_subjuntivo:
            frecuencias[verbo] = frecuencias.get(verbo, 0) + 1
        for verbo, frecuencia in frecuencias.items():
            writer.writerow([verbo, frecuencia])

def main():
    st.title("Buscador de Verbos en Modo Subjuntivo")
    texto = st.text_area("Ingresa el texto:")
    if st.button("Buscar verbos en modo subjuntivo"):
        verbos_subjuntivo = encontrar_verbos_subjuntivo(texto)
        if verbos_subjuntivo:
            st.write("Verbos en modo subjuntivo encontrados:")
            for verbo in verbos_subjuntivo:
                st.write(verbo)
            exportar_a_csv(verbos_subjuntivo)
            st.write("Resultados exportados a resultados.csv")
        else:
            st.write("No se encontraron verbos en modo subjuntivo.")

if __name__ == "__main__":
    main()

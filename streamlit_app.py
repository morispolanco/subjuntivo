import stanza
import streamlit as st

stanza.download('es')
nlp = stanza.Pipeline('es')

def extraer_subjuntivos(texto):
    doc = nlp(texto)
    subjuntivos = []

    for sent in doc.sentences:
        for word in sent.words:
            if 'Mood=Sub' in word.feats:
                subjuntivos.append(word.text)

    return subjuntivos

def main():
    st.title("Extracción de Subjuntivos en un Texto")
    st.write("Esta aplicación utiliza Stanza para extraer los subjuntivos en un texto en español.")

    texto = st.text_area("Ingrese un texto:")

    if st.button("Extraer Subjuntivos"):
        subjuntivos = extraer_subjuntivos(texto)
        st.write("Subjuntivos encontrados:")
        for subjuntivo in subjuntivos:
            st.write(subjuntivo)

if __name__ == "__main__":
    main()

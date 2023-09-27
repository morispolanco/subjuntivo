import streamlit as st
from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    subjunctive_count = 0
    for sentence in blob.sentences:
        if 'subjunctive' in sentence.tags:
            subjunctive_count += 1
    return subjunctive_count

def main():
    st.title("Análisis de texto con TextBlob")
    text = st.text_area("Ingrese el texto a analizar", "")
    if st.button("Analizar"):
        subjunctive_count = analyze_text(text)
        st.write("Cantidad de subjuntivos encontrados:", subjunctive_count)

if __name__ == "__main__":
    main()

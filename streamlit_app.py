import streamlit as st
import spacy


# Cargar el modelo de lenguaje SpaCy
nlp = spacy.load('es_core_news_sm')



def extract_verbs_subjunctive(text):
    doc = nlp(text)
    verbs = []
    subjunctive_verbs = []
    for token in doc:
        if token.pos_ == 'VERB':
            verbs.append(token.text)
            if token.morph.get('VerbForm') == 'Sub':
                subjunctive_verbs.append(token.text)
    return verbs, subjunctive_verbs


def app():
    st.title('Verbo y Modo Subjuntivo Extractor')
    st.write('Introduce el texto a analizar:')
    text = st.text_input('')
    verbs, subjunctive_verbs = extract_verbs_subjunctive(text)

    st.write('Verbos: ', verbs)
    st.write('Verbos en modo subjuntivo: ', subjunctive_verbs)


if __name__ == "__main__":
    app()

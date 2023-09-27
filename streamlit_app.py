import streamlit as st
import spacy

nlp = spacy.load('es_core_news_sm')

def count_subjunctive_verbs(text):
    doc = nlp(text)
    subjunctive_verbs = [token for token in doc if token.morph.get('Mood') == 'Sub']
    return len(subjunctive_verbs)

st.title('Contador de verbos en modo subjuntivo')

text = st.text_area('Ingresa el texto aquí:', '')

if st.button('Analizar texto'):
    count = count_subjunctive_verbs(text)
    st.write(f'El texto contiene {count} verbos en modo subjuntivo.')

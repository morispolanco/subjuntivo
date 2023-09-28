import streamlit as st
import spacy

nlp= spacy.load("es_core_news_md")

st.title('Buscador de verbos en subjuntivo')

text = st.text_area('Ingrese el texto a analizar:', height=200)

if text:
    doc = nlp(text)
    
    verbs_in_subjunctive = []
    
    for token in doc:
        if token.pos_ == 'VERB' and token.morph.get('Mood') == 'Sub':
            verbs_in_subjunctive.append(token.text)
            
    if verbs_in_subjunctive:
        st.write('Se encontraron los siguientes verbos en subjuntivo:')
        st.write(', '.join(verbs_in_subjunctive))
    else:
        st.write('No se encontraron verbos en subjuntivo.')

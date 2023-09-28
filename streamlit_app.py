# Importa las bibliotecas necesarias
import streamlit as st
from pattern.es import parse, split

# Crea una caja de texto en la interfaz de usuario de Streamlit
text = st.text_area("Ingresa el texto aquí")

# Analiza el texto con Pattern
parsed_text = parse(text)

# Divide el texto analizado en oraciones
sentences = split(parsed_text)

# Busca verbos en modo subjuntivo
subjunctive_verbs = []
for sentence in sentences:
    for word in sentence.words:
        if word.type.startswith('VB') and 'subjunctive' in word.mood:
            subjunctive_verbs.append(word.string)

# Muestra los verbos en modo subjuntivo
for verb in subjunctive_verbs:
    st.write(verb)

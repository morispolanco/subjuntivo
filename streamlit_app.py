import streamlit as st

def extract_subjunctive_verbs(text):
    subjunctive_verbs = []
    sentences = text.split(".")
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word.lower() in subjunctive_phrases:
                subjunctive_verbs.append(words[words.index(word) + 1])
    return subjunctive_verbs

subjunctive_phrases = [
    "Espero que", "Deseo que", "Ojalá que", "Sugiero que", "Recomiendo que",
    "Insisto en que", "Me alegra que", "Lamento que", "Es necesario que",
    "Es importante que", "Es fundamental que", "Es imprescindible que",
    "Es preferible que", "Es conveniente que", "Es urgente que", "Es posible que",
    "Es probable que", "Es dudoso que", "Es increíble que", "Es sorprendente que",
    "Es triste que", "Es justo que", "Es injusto que", "Es bueno que",
    "Es malo que", "Es mejor que", "Es peor que", "Es necesario que",
    "Es recomendable que", "Es válido que"
]

st.title("Extracción de verbos en modo subjuntivo")

text_input = st.text_area("Ingresa un texto:")
if st.button("Extraer verbos en modo subjuntivo"):
    subjunctive_verbs = extract_subjunctive_verbs(text_input)
    st.write("Verbos en modo subjuntivo encontrados:")
    for verb in subjunctive_verbs:
        st.write("- " + verb)

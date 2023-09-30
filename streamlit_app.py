import streamlit as st
from pattern.es import parse, split

def find_subjunctive_verbs(text):
    parsed_text = parse(text, lemmata=True)
    subjunctive_verbs = []
    for sentence in parsed_text.split():
        for i, (word, tag, _, lemma) in enumerate(sentence):
            if tag.startswith("VB") and "subj" in tag:
                if i > 0 and sentence[i-1][1] == "VB":
                    subjunctive_verbs.append(lemma)
    return subjunctive_verbs

def main():
    st.title("Extracción de verbos en subjuntivo")
    text = st.text_area("Ingrese un texto:")
    if st.button("Extraer verbos en subjuntivo"):
        subjunctive_verbs = find_subjunctive_verbs(text)
        st.write("Verbos en subjuntivo encontrados:")
        for verb in subjunctive_verbs:
            st.write(verb)

if __name__ == "__main__":
    main()

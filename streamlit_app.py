import streamlit as st
import re

def find_subjunctive_verbs(text):
    verbs = []
    words = text.split()
    for i in range(len(words) - 1):
        if words[i] == "que" and words[i+1].endswith("s"):
            verbs.append(words[i+1])
    return verbs

def main():
    st.title("Identificador de verbos en subjuntivo")
    st.write("Ingrese un texto en español para identificar los verbos en subjuntivo:")
    
    text = st.text_area("Texto")
    
    if st.button("Identificar verbos en subjuntivo"):
        subjunctive_verbs = find_subjunctive_verbs(text)
        st.write("Verbos en subjuntivo encontrados:")
        for verb in subjunctive_verbs:
            st.write(verb)

if __name__ == "__main__":
    main()

import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

# Descargar los datos necesarios de NLTK
nltk.download('punkt')

# Definir una función para encontrar verbos en subjuntivo
def find_subjunctive_verbs(text):
    # Tokenizar el texto
    tokens = word_tokenize(text, language='spanish')
    
    # Inicializar el stemmer
    stemmer = SnowballStemmer('spanish')
    
    # Filtrar los verbos en subjuntivo
    subjunctive_verbs = []
    for token in tokens:
        if token.endswith('r') and stemmer.stem(token) != token:
            subjunctive_verbs.append(token)
    
    return subjunctive_verbs

def main():
    st.title("Extracción de Verbos en Subjuntivo")
    text = st.text_area("Ingrese un texto en español:")
    
    if st.button("Buscar Verbos en Subjuntivo"):
        subjunctive_verbs = find_subjunctive_verbs(text)
        st.write("Verbos en Subjuntivo encontrados:")
        for verb in subjunctive_verbs:
            st.write(verb)

if __name__ == "__main__":
    main()

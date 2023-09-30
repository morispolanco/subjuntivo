import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import SnowballStemmer

# Descargar los datos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('omw')

# Definir una función para encontrar verbos en subjuntivo
def find_subjunctive_verbs(text):
    # Tokenizar el texto
    tokens = word_tokenize(text, language='spanish')
    
    # Realizar etiquetado gramatical
    pos_tags = nltk.pos_tag(tokens, lang='es')
    
    # Inicializar el stemmer
    stemmer = SnowballStemmer('spanish')
    
    # Filtrar los verbos en subjuntivo
    subjunctive_verbs = []
    for word, pos in pos_tags:
        if pos.startswith('V') and word.endswith('r') and stemmer.stem(word) != word:
            subjunctive_verbs.append((word, pos))
    
    return subjunctive_verbs

def main():
    st.title("Extracción de Verbos en Subjuntivo")
    text = st.text_area("Ingrese un texto en español:")
    
    if st.button("Buscar Verbos en Subjuntivo"):
        subjunctive_verbs = find_subjunctive_verbs(text)
        st.write("Verbos en Subjuntivo encontrados:")
        for verb, pos in subjunctive_verbs:
            st.write(f"{verb} ({pos})")

if __name__ == "__main__":
    main()

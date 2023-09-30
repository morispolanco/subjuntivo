import streamlit as st
import docx2txt
import re
import csv

def find_subjunctive_verbs(text):
    verbs = []
    words = text.split()
    for i in range(len(words) - 1):
        if words[i] == "que" and words[i+1].endswith("s"):
            verbs.append(words[i+1])
    return verbs

def count_subjunctive_verbs(file_path):
    text = docx2txt.process(file_path)
    subjunctive_verbs = find_subjunctive_verbs(text)
    return len(subjunctive_verbs)

def main():
    st.title("Identificador de verbos en subjuntivo")
    st.write("Cargue un archivo .docx para identificar los verbos en subjuntivo:")
    
    file = st.file_uploader("Cargar archivo .docx", type=["docx"])
    
    if file is not None:
        file_path = file.name
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        
        num_verbs = count_subjunctive_verbs(file_path)
        
        st.write("Número de verbos en subjuntivo encontrados:", num_verbs)
        
        with open("verbos_subjuntivo.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Archivo", "Número de verbos en subjuntivo"])
            writer.writerow([file_path, num_verbs])

if __name__ == "__main__":
    main()

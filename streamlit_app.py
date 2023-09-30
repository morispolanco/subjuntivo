import streamlit as st
import spacy

def find_subjunctive_verbs(text):
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(text)
    subjunctive_verbs = []
    for token in doc:
        if token.pos_ == "VERB" and token.morph.get("Mood") == "Sub":
            subjunctive_verbs.append(token.lemma_)
    return subjunctive_verbs

text = "Espero que tú vengas a la fiesta."
subjunctive_verbs = find_subjunctive_verbs(text)
print(subjunctive_verbs)

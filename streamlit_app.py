import streamlit as st
from pattern.es import parse, split

def find_subjunctive_verbs(text):
    parsed_text = parse(text, lemmata=True)
    subjunctive_verbs = []
    for sentence in parsed_text.split():
        for word, tag, _, lemma in sentence:
            if tag.startswith("VB") and "subj" in tag:
                subjunctive_verbs.append(lemma)
    return subjunctive_verbs

text = "quiero que estudies y seas rico"

subjunctive_verbs = find_subjunctive_verbs(text)

print("Verbos en subjuntivo encontrados:")
for verb in subjunctive_verbs:
    print(verb)

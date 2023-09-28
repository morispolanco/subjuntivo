import streamlit as st
import spacy
import re

nlp = spacy.load("es_core_news_sm")

def extract_subjunctive_verbs_from_file(filename):
  """Extracts subjunctive verbs from a Spanish text file.

  Args:
    filename: The path to the Spanish text file.

  Returns:
    A list of subjunctive verbs.
  """

  subjunctive_verbs = []
  with open(filename, "r", encoding="utf-8") as f:
    text = f.read()
    doc = nlp(text)
    for token in doc:
      if token.pos == "VERB" and token.tag == "SUBJ":
        subjunctive_verbs.append(token.text)
  return subjunctive_verbs

filename = "spanish_text.txt"

subjunctive_verbs = extract_subjunctive_verbs_from_file(filename)

print(subjunctive_verbs)

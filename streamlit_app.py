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

def main():
  """Renders the Streamlit app."""

  st.title('Spanish Subjunctive Verb Extractor')

  filename = st.text_input('Enter the path to a Spanish text file:')
  if filename:
    subjunctive_verbs = extract_subjunctive_verbs_from_file(filename)
    if subjunctive_verbs:
      st.write('\n## Subjunctive verbs:')
      for verb in subjunctive_verbs:
        st.write(verb)
    else:
      st.write('No subjunctive verbs found.')

if __name__ == '__main__':
  main()

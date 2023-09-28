import streamlit as st
import spacy
import re

nlp = spacy.load("es_core_news_sm")

def extract_subjunctive_verbs_from_text(text):
  """Extracts subjunctive verbs from a Spanish text.

  Args:
    text: A Spanish text.

  Returns:
    A list of subjunctive verbs.
  """

  subjunctive_verbs = []
  doc = nlp(text)
  for token in doc:
    if token.pos == "VERB" and token.tag == "SUBJ":
      subjunctive_verbs.append(token.text)
  return subjunctive_verbs

def main():
  """Renders the Streamlit app."""

  st.title('Spanish Subjunctive Verb Extractor')

  text = st.text_area('Enter a Spanish text:')
  if text:
    subjunctive_verbs = extract_subjunctive_verbs_from_text(text)
    if subjunctive_verbs:
      st.write('\n## Subjunctive verbs:')
      for verb in subjunctive_verbs:
        st.write(verb)
    else:
      st.write('No subjunctive verbs found.')

if __name__ == '__main__':
  main()

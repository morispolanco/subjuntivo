import streamlit as st
import re

def extract_subjunctive_verbs(text):
  """Extracts verbs in the subjunctive mode from a Spanish text.

  Args:
    text: A Spanish text.

  Returns:
    A list of subjunctive verbs in the text.
  """

  subjunctive_verb_regex = re.compile(r'\b(que|ojalá|quizá(s)|tal vez|acaso|espero|quiero|deseo|necesito|es importante que|es necesario que|es mejor que|es preferible que|es recomendable que|es obligatorio que|es aconsejable que|es posible que|es probable que|es dudoso que|es difícil que|es fácil que|no|nunca)\s+(sea|seas|sea|seamos|sean|estemos|estén|esté|fuera|fueras|fuera|fuéramos|fueran|estuviera|estuvieras|estuviera|estuviéramos|estuvieran|haya|hayas|haya|hayamos|hayan|hubiera|hubieras|hubiera|hubiéramos|hubieran|vengamos|estemos|estén|estemos)\s+\w+\b', re.IGNORECASE)
  subjunctive_verbs = []
  for match in subjunctive_verb_regex.finditer(text):
    verb = match.group(3)
    # Remove the trailing infinitive marker, if any.
    verb = verb.rstrip('r')
    # Add the verb to the list, if it is not already there.
    if verb not in subjunctive_verbs:
      subjunctive_verbs.append(verb)
  return subjunctive_verbs

def main():
  """Renders the Streamlit app."""

  text = st.text_area('Enter a Spanish text:')
  if text:
    subjunctive_verbs = extract_subjunctive_verbs(text)
    if subjunctive_verbs:
      st.write('\n## Subjunctive verbs:')
      for verb in subjunctive_verbs:
        st.

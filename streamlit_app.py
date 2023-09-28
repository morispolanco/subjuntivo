import streamlit as st
import re

def extract_subjunctive_verbs(text):
  """Extracts verbs in the subjunctive mode from a Spanish text.

  Args:
    text: A Spanish text.

  Returns:
    A list of subjunctive verbs in the text.
  """

  subjunctive_verb_regex = re.compile(r'\b(que|ojalá|quizá(s)|tal vez|acaso|espero|quiero|deseo|necesito|es importante que|es necesario que|es mejor que|es preferible que|es recomendable que|es obligatorio que|es aconsejable que|es posible que|es probable que|es dudoso que|es difícil que|es fácil que)\s+(sea|seas|sea|seamos|sean|estuviera|estuvieras|estuviera|estuviéramos|estuvieran|haya|hayas|haya|hayamos|hayan|hubiera|hubieras|hubiera|hubiéramos|hubieran)\s+\w+\b', re.IGNORECASE)
  subjunctive_verbs = []
  for match in subjunctive_verb_regex.finditer(text):
    subjunctive_verbs.append(match.group(1))
  return subjunctive_verbs

def main():
  """Renders the Streamlit app."""

  st.title('Spanish Subjunctive Verb Extractor')

  text = st.text_area('Enter a Spanish text:')
  if text:
    subjunctive_verbs = extract_subjunctive_verbs(text)
    if subjunctive_verbs:
      st.write('\n## Subjunctive verbs:')
      for verb in subjunctive_verbs:
        st.write(verb)
    else:
      st.write('No subjunctive verbs found.')

if __name__ == '__main__':
  main()

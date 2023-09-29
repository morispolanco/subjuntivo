import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Define a function to find verbs in subjunctive mood
def find_subjunctive_verbs(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Perform part-of-speech tagging
    pos_tags = nltk.pos_tag(tokens)
    
    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Filter out non-verbs
    verbs = [(word, pos) for word, pos in pos_tags if pos.startswith('V')]
    
    # Filter out verbs not in the subjunctive mood
    subjunctive_verbs = []
    for word, pos in verbs:
        # Use WordNet to find synonyms of the verb
        synonyms = wordnet.synsets(word, pos=get_wordnet_pos(pos))
        if synonyms:
            synonym = synonyms[0]
            lemma = lemmatizer.lemmatize(word, get_wordnet_pos(pos))
            # Check if the verb is in the subjunctive mood
            if lemma in synonym.lemmas()[0].name().split('/'):
                subjunctive_verbs.append((word, pos))
    
    return subjunctive_verbs

# Function to get the WordNet part-of-speech
def get_wordnet_pos(nltk_pos):
    if nltk_pos.startswith('J'):
        return wordnet.ADJ
    elif nltk_pos.startswith('V'):
        return
        wordnet.VERB
elif nltk_pos.startswith('N'):
return wordnet.NOUN
elif nltk_pos.startswith('R'):
return wordnet.ADV
else:
return None

Initialize Streamlit app
st.set_page_config(page_title="Find Subjunctive Verbs in Spanish Text", page_icon=":spiral_notepad:", layout="wide")

Create an input field for the text
st.title("Find Subjunctive Verbs in Spanish Text")
text_input = st.text_input("Paste your Spanish text here", "")

Create a button to trigger the analysis
button = st.button("Analyze Text")

Display the results
if button:
subjunctive_verbs = find_subjunctive_verbs(text_input)
st.success("Subjunctive Verbs Found:")
st.write(subjunctive_verbs)

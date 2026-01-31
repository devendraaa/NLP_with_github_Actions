from textblob import TextBlob
import wikipedia



def search_wikipedia(name):
    print(f"Searching wikipedia for name: {name}")
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """Summarize wikipedia """
    print(f"Finding wikipedia summary for a name :{name}")
    return wikipedia.summary(name)

def get_text_blob(text):
    """Gets text blob object and return"""

    blob = TextBlob(text)
    return blob

def get_phrase(name):
    """finding wikipedia name and return back phrase"""

    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases

golden_state_warriors_text = wikipedia.summary("Golden State Warriors")

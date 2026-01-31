from nlplogic.corenlp import get_phrase, summarize_wikipedia, search_wikipedia, get_text_blob

def test_search():
    assert  'golden state' in get_phrase("Golden State Warriors")
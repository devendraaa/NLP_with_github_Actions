from nlplogic.corenlp import get_phrase

def test_search():
    assert  'golden state' in get_phrase("Golden State Warriors")
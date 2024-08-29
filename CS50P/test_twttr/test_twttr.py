from twttr import shorten

def test_shorten():
    assert shorten("string") == "strng"
    assert shorten("STRING") == "STRNG"
    assert shorten("0") == "0"
    assert shorten(".") == "."

from twttr import shorten

def test_lower():
    assert shorten("sade") == "sd"

def test_upper():
    assert shorten("SADE") == "SD"

def test_number():
    assert shorten("SADE1") == "SD1"

def test_punctuation():
    assert shorten("SADE!") == "SD!"
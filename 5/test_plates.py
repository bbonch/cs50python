from plates import is_valid

def test_starts_with_two_letters():
    assert is_valid("s111") == False

def test_len():
    assert is_valid("ss") == True
    assert is_valid("ss1111") == True
    assert is_valid("sss1111") == False

def test_numbers():
    assert is_valid("ss111s") == False
    assert is_valid("ssss01") == False
    assert is_valid("ssss11") == True

def test_punctuayion():
    assert is_valid("ss 111") == False
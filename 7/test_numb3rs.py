from numb3rs import validate

def test_1():
    assert validate("cat") == False
    assert validate("s.d.f.g") == False
    assert validate("0.0.00") == False
    assert validate("0.0.0..0") == False

def test_2():
    assert validate("0.3.64.255") == True
    assert validate("256.6.6.6") == False
    assert validate("251.633.644.656") == False
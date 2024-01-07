from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hi") == 20

def test_other():
    assert value("cat") == 100

def test_case():
    assert value("hEllO") == 0
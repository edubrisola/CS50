from plates import is_valid

def test_isvalid():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True

def test_isinvalid():
    assert is_valid("CS50A") == False
    assert is_valid("A2") == False
    assert is_valid("50CS") == False
    assert is_valid("CS05") == False
    assert is_valid("CSCSCSCS") == False
    assert is_valid("50") == False
    assert is_valid("CS.,10") == False
    assert is_valid("c") == False
    assert is_valid("hello, world") == False

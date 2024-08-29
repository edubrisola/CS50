from numb3rs import validate

def test_values_true():
    assert validate("127.0.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_values_false():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.256.0.0") == False
    assert validate("1.1.256.0") == False
    assert validate("cat") == False


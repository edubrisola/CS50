from jar import Jar

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(4)
    assert jar.capacity == 4
    jar = Jar(1)
    assert jar.capacity == 1

def test_string():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit_withdraw():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(6)
    assert jar.size == 8
    jar.withdraw(6)
    assert jar.size == 2
    jar.withdraw(1)
    assert jar.size == 1

def test_size():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(1)
    assert jar.size == 5

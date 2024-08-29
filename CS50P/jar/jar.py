class Jar():

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        symbols = "🍪" * self.size
        return symbols


    def deposit(self, n):
        if (self.size + n) <= self.capacity and n <= self.capacity:
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if (self.size - n) >= 0 and n >= 0:
            self._size -= n
        else:
            raise ValueError


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

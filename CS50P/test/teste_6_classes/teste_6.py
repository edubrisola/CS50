class Buckets():
    def __init__(self, water=0, oil=0, solid=0):
        self.water = water
        self.oil = oil
        self.solid = solid

    def __str__(self):
        return f"{self.water}, {self.oil}, {self.solid}"

    def __add__(self, other):
        water = self.water + other.water
        oil = self.oil + other.oil
        solid = self.solid + other.solid
        return Buckets(water, oil, solid)


first = Buckets(100, 50, 25)
print(first)

second = Buckets(25, 50, 10)
print(second)

total = first + second
print(total)




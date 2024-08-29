class Students():
    def __init__(self, name, house, birth):
        self.name = name
        self.house = house
        self.birth = birth

    def getage(self):
        return 2024 - self.birth

def main():
    harry = Students("Harry Potter", "Gryffindor", 1981)

    print(harry.name, harry.house, harry.birth, harry.getage())
    return

if __name__ == "__main__":
    main()

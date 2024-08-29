def main():
    mass = float(input("Mass: "))
    energy = int(mass_energy(mass))
    print(energy)

def mass_energy(mass):
    return (mass * (300000000 ** 2))

if __name__ == "__main__":
    main()

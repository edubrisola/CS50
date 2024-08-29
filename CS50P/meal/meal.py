def main():
    string = input("What time is it? ")
    hour = convert(string)


    if hour >= 7 and hour <= 8:
        print("breakfast time")
    elif hour >= 12 and hour <= 13:
        print("lunch time")
    elif hour >= 18 and hour <= 19:
        print("dinner time")

def convert(string):
    hours, minutes = string.split(":")

    hours = float(hours)
    minutes = float(minutes)

    minutes /= 60

    return hours + minutes


if __name__ == "__main__":
    main()

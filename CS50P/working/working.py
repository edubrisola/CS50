import re


def main():
    print(convert(input("Hours: ").strip()))


def convert(string):

    pattern = r"^([0-9]{1,2})(?::([0-9]{2}))?\s(AM|PM)\s+to\s+([0-9]{1,2})(?::([0-9]{2}))?\s(AM|PM)$"
    matches = re.match(pattern, string)

    if not matches:
        raise ValueError("Invalid time format")

    hour1, min1, meridiem1, hour2, min2, meridiem2 = matches.groups()

    if int(hour1) not in range(1, 13) or (min1 and int(min1) not in range(0, 60)):
        raise ValueError("Invalid time")
    if int(hour2) not in range(1, 13) or (min2 and int(min2) not in range(0, 60)):
        raise ValueError("Invalid time")

    hour1 = int(hour1)
    hour2 = int(hour2)

    if meridiem1 == 'PM' and hour1 != 12:
        hour1 += 12
    elif meridiem1 == 'AM' and hour1 == 12:
        hour1 = 0

    if meridiem2 == 'PM' and hour2 != 12:
        hour2 += 12
    elif meridiem2 == 'AM' and hour2 == 12:
        hour2 = 0

    min1 = min1 if min1 else '00'
    min2 = min2 if min2 else '00'
    return f"{hour1:02}:{min1} to {hour2:02}:{min2}"


if __name__ == "__main__":
    main()

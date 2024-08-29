import datetime
import re
import sys
import inflect


class year():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getminutes(self):
        minutes_now = datetime.date.today()
        minutes_date = datetime.date(self.year, self.month, self.day)
        minutes = minutes_now - minutes_date

        return (round(minutes.total_seconds() / 60))


def main():

    p = inflect.engine()

    string = input("Date: ").strip()
    date = getinput(string)

    minutes = date.getminutes()

    minutes = p.number_to_words(minutes, andword="")
    minutes = minutes.capitalize()
    print(f"{minutes} minutes")


def getinput(string):
    matches = re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", string)
    if matches:
        date = year(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))

        if (date.month > 12 or date.month < 0) or (date.day > 31 or date.day < 0):
            print("Invalid date")
            sys.exit(1)
        else:
            return date
    else:
        print("Invalid date")
        sys.exit(1)


if __name__ == "__main__":
    main()

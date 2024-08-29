def main():

    MONTHS = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        try:
            date = input("Date: ").strip()

            # If MM/DD/YYYY
            if date.count("/") == 2:
                month, day, year = date.split("/")
                day = int(day)
                month_number = int(month)

                if day > 31:
                    continue

                elif month_number not in MONTHS.values():
                    continue

                else:
                    if day < 10:
                        if month_number < 10:
                            print(f"{year}-0{month_number}-0{day}")
                        else:
                            print(f"{year}-{month_number}-0{day}")
                    elif day >= 10:
                        if month_number < 10:
                            print(f"{year}-0{month_number}-{day}")
                        else:
                            print(f"{year}-{month_number}-{day}")

                break

            # If M D, YYYY
            elif date.count(",") == 1:
                date = date.replace(",", "")
                month, day, year = date.split()
                month = month.title()
                month_number = 0
                day = int(day)

                if month in MONTHS:
                    month_number = MONTHS[month]

                elif month not in MONTHS:
                    continue

                elif day > 31:
                    continue

                else:
                    if day < 10:
                        if month_number < 10:
                            print(f"{year}-0{month_number}-0{day}")
                        else:
                            print(f"{year}-{month_number}-0{day}")
                    elif day >= 10:
                        if month_number < 10:
                            print(f"{year}-0{month_number}-{day}")
                        else:
                            print(f"{year}-{month_number}-{day}")

                break

            else:
                continue

        except ValueError:
            pass

if __name__ == "__main__":
    main()

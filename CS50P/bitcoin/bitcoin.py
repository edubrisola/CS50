import json
import requests
import sys

def main():
    args = len(sys.argv)

    if args != 2:
        print("Missing command-line argument")
        sys.exit(1)

    elif args == 2:

        while True:
            try:
                if sys.argv[1].isalpha():
                    print("Command-line argument is not a number")
                    sys.exit(1)

                number = float(sys.argv[1])
            except ValueError:
                print("Command-line argument is not a number")
                sys.exit(1)

            requested = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            requested = requested.json()

            print(requested)
            price = float(requested["bpi"]['USD']['rate_float'])

            integer = str(number * price)
            integer = float(integer)


            print(f"${integer:,}")

            sys.exit(0)


if __name__ == "__main__":
    main()

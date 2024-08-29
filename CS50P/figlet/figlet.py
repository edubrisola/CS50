from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()
args = len(sys.argv)

if args == 1 or args == 3:
    if args == 3 and sys.argv[2] in fonts and sys.argv[1] in ["-f", "--font"]:
        string = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(string))
        sys.exit(0)

    elif args == 1 and sys.argv[0] == 'figlet.py':
        string = input("Input: ")
        f = random.choice(fonts)
        figlet.setFont(font=f)
        print(figlet.renderText(string))
        sys.exit(0)

    else:
        print("Invalid usage")
        sys.exit(1)

else:
    print("Invalid usage")
    sys.exit(1)

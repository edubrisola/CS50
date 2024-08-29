import sys
import re

def main():
    string = input("HTML: ")
    print(parse(string))
    return

def parse(ip):
    matches = re.search(r"^(<iframe[^>]+src=\")?https?://(www\.)?youtube\.com/embed/([^\"]+)\"?(></iframe>)?$", ip, re.IGNORECASE)
    if matches:
        id = matches.group(3)
        return f"https://youtu.be/{id}"
    return None


if __name__ == "__main__":
    main()

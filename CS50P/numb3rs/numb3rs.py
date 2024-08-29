def main():
    address = input("IPv4 Address: ").strip()

    if validate(address):
        print("True")
        return
    else:
        print("False")


def validate(ip):
    if ip.count(".") != 3:
        return False
    else:
        num1, num2, num3, num4 = ip.split(".")

        if 0 <= int(num1) <= 255 and 0 <= int(num2) <= 255 and 0 <= int(num3) <= 255 and 0 <= int(num4) <= 255:
            return True
        else:
            return False


if __name__ == "__main__":
    main()

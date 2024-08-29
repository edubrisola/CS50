def main():
    NAMES = [
        { 'name': "Eduardo", 'phone': '45 99822-0343'},
        { 'name': "Vinicius", 'phone': '45 99946-4961'},
        { 'name': "Anna", 'phone': '45 99911-0053'}
    ]

    while True:
        try:
            string = input("Name: ").title().strip()

            if string == '':
                break

        except ValueError:
            pass

        if string in NAMES:
            print(f"Phone: {NAMES[string]}")
            break
        break

    OTHER = {'name': "Tanaka", 'phone': '45 99888-0076'}
    NAMES.append(OTHER)
    NAMES = sorted(NAMES, key=lambda x: x['name'])

    for contact in NAMES:
        print(f"Name: {contact['name']} || Phone: {contact['phone']}")


if __name__ == "__main__":
    main()

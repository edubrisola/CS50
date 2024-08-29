from cs50 import SQL
import hashlib
import random

def main():

    db = SQL("sqlite:///passwords.db")

    getInput(db)


def getInput(db):
    print()

    while True:
        try:
            print("1. Register\n2. login\n3. Delete Account\n")
            option = input("Option: ").strip()

            if option.isnumeric():
                option = int(option)

                if option == 1:
                    register(db)
                    continue
                elif option == 2:
                    login(db)
                    continue
                elif option == 3:
                    deleter(db)
                    continue
                else:
                    print("\nInvalid Option!\n")
                    continue

            elif option.isalpha():
                option = option.lower()

                if option == "register":
                    register(db)
                    continue
                elif option == "login":
                    login(db)
                    continue
                elif option == "delete" or option == "delete account":
                    deleter(db)
                    continue
                else:
                    print("\nInvalid Option!\n")
                    continue

            elif option == "":
                break

            else:
                print("\nInvalid Option!\n")
                continue

        except ValueError:
            pass
    return


def login(db):
    while True:
        name = input("Name: ").lower()

        if name == "":
            continue

        name = hash_code(name)

        while True:
            password = input("Password: ")

            if password == "":
                continue
            else:
                break

        break

    if name_confirmation(db, name):
        print("\nUser Not Found!\n")
        return

    salt = db.execute("SELECT id_salt FROM people WHERE person_id = ?", name)
    salt = salt[0]["id_salt"]
    password = hash_code(salt + password)

    password_confirmation = db.execute("SELECT id_key FROM people WHERE person_id = ?", name)
    password_id = password_confirmation[0]["id_key"]

    if password == password_id:
        print("\nSuccesfull Login!\n")
    else:
        print("\nWrong Password! Try Again!\n")
    return


def register(db):
    while True:
        name = input("Name (In Lowercase): ").lower()

        if name == "":
            continue

        name = hash_code(name)

        while True:
            password = input("Password (Symbols, Lowercase, Uppercase, Numbers): ")

            if password == "":
                continue
            else:
                break

        break

    salt = str(random.randint(0, 100000000000000))
    password = salt + password
    password = hash_code(password)

    if name_confirmation(db, name):
        db.execute("INSERT INTO people (person_id, id_key, id_salt) VALUES (?, ?, ?);", name, password, salt)
        print("\nSuccesfull Register!\n")
        return

    else:
        print("\nTry Another User Name!\n")
        return


def deleter(db):
    while True:
        name = input("Name: ").lower()

        if name == "":
            continue

        name = hash_code(name)

        while True:
            password = input("Password: ")

            if password == "":
                continue
            else:
                break

        break

    if name_confirmation(db, name):
        print("\nUser Not Found!\n")
        return

    salt = db.execute("SELECT id_salt FROM people WHERE person_id = ?", name)
    salt = salt[0]["id_salt"]
    password = hash_code(salt + password)

    password_confirmation = db.execute("SELECT id_key FROM people WHERE person_id = ?", name)
    password_id = password_confirmation[0]["id_key"]

    if password == password_id:
        db.execute("DELETE FROM people WHERE id_key = ? AND person_id = ?", password, name)
        print("\nSuccesfull Deleting!\n")
    else:
        print("\nWrong Password! Try Again!\n")
    return


def name_confirmation(db, name):
    name_confirmation = db.execute("SELECT person_id FROM people WHERE person_id = ?", (name,))

    if name_confirmation:
         return False
    else:
        return True

def hash_code(string):
    sha256 = hashlib.sha256()

    sha256.update(string.encode("utf-8"))

    return sha256.hexdigest()


if __name__ == "__main__":
     main()


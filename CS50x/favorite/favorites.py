from cs50 import SQL

db = SQL("sqlite:///shows.db")

favorite = input("Name: ")

# Primeiro, obtenha o ID da pessoa com base no nome fornecido
person = db.execute("SELECT id FROM people WHERE name = ?", favorite)

if not person:
    print("Person not found")
else:
    person_id = person[0]["id"]

    # Em seguida, obtenha os IDs dos shows estrelados por essa pessoa
    shows = db.execute("SELECT show_id FROM stars WHERE person_id = ?", person_id)

    if not shows:
        print("No shows found for this person")
    else:
        # Obtenha os títulos dos shows com base nos IDs dos shows obtidos
        for show in shows:
            show_id = show["show_id"]
            titles = db.execute("SELECT title FROM shows WHERE id = ?", show_id)

            # Exibe todos os títulos encontrados
            for title in titles:
                print(title["title"])

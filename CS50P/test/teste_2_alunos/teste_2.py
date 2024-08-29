def main():

    ALUNOS = {}

    inputDic(ALUNOS)
    imprimeDic(ALUNOS)


def inputDic(ALUNOS):

    while True:
        try:
            nome = input("Nome: ")

            if nome.isnumeric():
                print("Nome Inválido!")
                continue
            elif nome == '':
                break

            nota = input("Nota: ")

            if nota.isnumeric():
                nota = int(nota)

                if nome not in ALUNOS:
                    ALUNOS[nome] = nota
                else:
                    print("Aluno Repetido!")
                    continue

                continue

            else:
                print("Nota Inválida!")
                continue

        except ValueError:
            pass


def imprimeDic(ALUNOS):
    for alunos in ALUNOS:
        print(f"Aluno: {alunos} || Nota: {ALUNOS[alunos]}")


if __name__ == "__main__":
    main()

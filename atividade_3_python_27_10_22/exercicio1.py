# Crie um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Programa Turno alunos")
turno = str(input("Olá aluno, em que turno você estuda? Digite M (Matutino), V (Vespertino) ou N (Noturno): ")).upper()

match turno:
    case "M":
        print("Bom dia !")

    case "V":
        print("Boa tarde !")

    case "N":
        print("Boa noite !")

    case _:
        print("Valor inválido ! Digite somente M, V ou N.")

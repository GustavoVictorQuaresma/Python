# Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# Mostre as consoantes.

print("Programa vetor caracteres")

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    lista[i] = str(input("Digite 10 letras de A até Z: "))
print("A lista de caracteres é: ", lista)

def vogal (lista):
    soma = 0
    for i in lista:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            continue
        else:
            soma += 1
    print("A quantidade de consoante é: ", soma)
    return soma

vogal(lista)
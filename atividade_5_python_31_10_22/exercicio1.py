# Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# Mostre as consoantes.

print("Programa vetor caracteres")

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
vogais = ["a", "e", "i", "o", "u"]

for i in range(10):
    lista[i] = str(input("Digite 10 letras de A até Z: ")).upper()

c1 = str(input("Digite uma consoante para localizar: ")).upper()
encontrado = False

for i in range(10):
        if lista[i] == c1:
            print("A consoante", c1, "foi encontrada na posição ", i)
            encontrado = True

if encontrado is False:
    print("Não foi encontrada a consoante", c1, " na busca !")

print(lista)
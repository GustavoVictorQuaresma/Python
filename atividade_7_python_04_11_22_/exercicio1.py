# Faça um Programa que leia dois vetores com 10 posições cada e receba números inteiros.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados
# dos dois outros vetores. Mostre ao final os três vetores.

from itertools import chain
print("Programa Dois Vetores")

vetor1 = []
for i in range(10):
    inteiro1 = int(input("Digite 10 números inteiros para o primeiro vetor: "))
    vetor1.append(inteiro1)

vetor2 = []
for i in range(10):
    inteiro2 = int(input("Digite 10 números inteiros para o segundo vetor: "))
    vetor2.append(inteiro2)

vetor3 = list(chain.from_iterable(zip(vetor1, vetor2)))

print("O primeiro vetor recebeu os seguintes números: ", vetor1)
print("O segundo vetor recebeu os seguintes números: ", vetor2)
print("O terceiro vetor recebeu os seguintes números intercalados: ", vetor3)




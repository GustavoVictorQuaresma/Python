# Faça um programa que calcule o fatorial de um número, é obrigatório o uso de função recursiva para o calculo fatorial.

print("Programa Fatorial")

n = int(input("Digite um número inteiro para fazer o calculo fatorial: "))

def fatorial(n):
   if n == 1 or n == 0:
       return 1
   else:
       return n*fatorial(n-1)

if n < 0:
   print("Valor inválido ! Digite somente números inteiros positivos !")
else:
   print("O calculo fatorial de", n, "é", fatorial(n))
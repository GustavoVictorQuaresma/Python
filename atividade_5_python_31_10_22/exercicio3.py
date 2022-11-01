# Crie um programa com uma função para multiplicar dois números e o algoritmo mostrar o resultado.

print("Programa Multiplicação")

def multiply(n1, n2):
    resultado = n1 * n2
    return resultado

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
resultado = multiply(n1, n2)
print("O resultado da multiplicação dos dois números é: ", resultado)
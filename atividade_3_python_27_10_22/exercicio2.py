# Crie um programa para realizar as operações de uma tabuada de multiplicação, onde será solicitado ao usuário digitar
# qual numero será a tabuada e qual intervalo do inicio e fim da tabuada, e exibir na tela o resultado conforme intervalo.

# Repetição usando “PARA”
# for i in n:
# for i in range(10):

print("Programa Tabuada de multiplicação")
num1 = int(input("Digite um número inteiro para escolher qual tabuada você deseja visualizar: "))
print("Você escolheu a tabuada do número:", num1)

inicio = int(input("Digite um número inteiro para o intervalo do inicio da tabuada: "))
fim = int(input("Digite um número inteiro para o intervalo do final da tabuada: "))

for i in range(inicio,fim+1):
    print(num1*i)
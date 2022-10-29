# Crie um programa em que o usuário deve digitar números inteiros para uma matriz de 5 linhas e 5 colunas .
# Após a digitação dos números, o usuário deve digitar um número aleatório e verificar se ele se encontra na matriz.
# Ao final, os índices da linha e da coluna devem ser impressos se o elemento for encontrado;
# caso contrário, a mensagem “elemento não encontrado” deve ser mostrada na tela.

print("Programa Matriz")

M = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
for i in range(4):
    for j in range(4):
        M[i][j] = int(input("Digite os números inteiros para adicionar na matriz: "))

num = int(input("Digite um número inteiro para procurar na matriz: "))

for i in range(4):
    for j in range(4):
        if M[i][j] == num:
            print("Numéro encontrado !")

        else:
            print("Número não encontrado !")

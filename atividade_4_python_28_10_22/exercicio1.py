# Crie um programa para calcular as notas obtidas pelo aluno do ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado, se está em recuperação ou
# foi reprovado sem chance de recuperação.
# Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos.

print("Programa Notas obtidas pelos alunos do Ensino Médio")

b1 = int(input("Digite a nota do 1° bimestre: "))
if (b1>25):
    print("Valor inválido ! O bimestre vale 25 pontos !")
else:
    print(b1)
b2 = int(input("Digite a nota do 2° bimestre: "))
if (b2>25):
    print("Valor inválido ! O bimestre vale 25 pontos !")
else:
    print(b2)
b3 = int(input("Digite a nota do 3° bimestre: "))
if (b3>25):
    print("Valor inválido ! O bimestre vale 25 pontos !")
else:
    print(b3)
b4 = int(input("Digite a nota do 4° bimestre: "))
if (b4>25):
    print("Valor inválido ! O bimestre vale 25 pontos !")
else:
    print(b4)
resultado = b1+b2+b3+b4
if (resultado>100):
    print("Valor inválido ! A soma dos 4 bimestres tem um total de até 100 pontos !")
elif (resultado>=60 and resultado<=100):
    print("Você foi aprovado !")
elif (resultado<40 and resultado>=0):
    print("Você foi reprovado !")
elif (resultado>40 and resultado<60):
    print("Você está de recuperação !")


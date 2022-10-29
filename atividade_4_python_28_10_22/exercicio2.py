# Crie um programa para calcular as notas obtidas pelo aluno do ensino médio, deverá mostrar mensagem para ser digitado
# a nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho. Após deverá mostrar na tela a média obtida
# no 1º, 2º, 3º e 4ºbimestre.
# E depois o total informado se o aluno foi aprovado, esta em recuperação ou foi reprovado sem recuperação.

print("Programa Notas obtidas pelos alunos do Ensino Médio")

p1 = float(input("Digite a nota da 1ª prova do 1° bimestre: "))
print(p1)
t1 = float(input("Digite a nota do 1° trabalho do 1° bimestre: "))
print(t1)
b1 = p1 + t1
if (b1>25):
    print("Valor inválido ! O bimestre vale 25 pontos !")
else:
    print("A nota obtida no 1ª bimestre foi:", b1)
media1 = b1/2
print("A nota média obtida no 1° bimestre foi:", media1)
p2 = float(input("Digite a nota da 1ª prova do 2° bimestre: "))
print(p2)
t2 = float(input("Digite a nota do 1° trabalho do 2° bimestre: "))
print(t2)
b2 = p2 + t2
if (b2>25):
    print("Valor inválido ! O bimestre vale 25 pontos !")
else:
    print("A nota obtida no 2ª bimestre foi:", b2)
media2 = b2/2
print("A nota média obtida no 2° bimestre foi:", media2)
p3 = float(input("Digite a nota da 1ª prova do 3° bimestre: "))
print(p3)
t3 = float(input("Digite a nota do 1° trabalho do 3° bimestre: "))
print(t3)
b3 = p3 + t3
if (b3>25):
    print("Valor inválido ! O bimestre vale 25 pontos !")
else:
    print("A nota obtida no 3° bimestre foi:", b3)
media3 = b3/2
print("A nota média obtida no 3° bimestre foi:", media3)
p4 = float(input("Digite a nota da 1ª prova do 4° bimestre: "))
print(p4)
t4 = float(input("Digite a nota do 1° trabalho do 4° bimestre: "))
print(t4)
b4 = p4 + t4
if (b4>25):
    print("Valor inválido ! O bimestre vale 25 pontos !")
else:
    print("A nota obtida no 4ª bimestre foi:", b4)
media4 = b4/2
print("A nota média obtida no 4° bimestre foi:", media4)
mediatotal = (b1+b2+b3+b4)/4
print("A nota média obtida em todos os 4 bimestres foi:", mediatotal)
resultado = b1+b2+b3+b4
if (resultado>100):
    print("Valor inválido ! A soma dos 4 bimestres tem um total de até 100 pontos !")
elif (resultado>=60 and resultado<=100):
    print("Você foi aprovado !")
elif (resultado<40 and resultado>=0):
    print("Você foi reprovado !")
elif (resultado>40 and resultado<60):
    print("Você está de recuperação !")
# Programa recebe 5 produtos em variáveis constantes

v1 = 2980.0
v2 = 2540.0
v3 = 1950.0
v4 = 2100.0
v5 = 2350.0

qtdev1= float(input("Digite a quantidade de iPhone que você deseja comprar, se não quiser nenhum, digite 0:"))
resultadov1 = qtdev1 * v1
print(resultadov1)

qtdev2= float(input("Digite a quantidade de Samsung que você deseja comprar, se não quiser nenhum, digite 0:"))
resultadov2 = qtdev2 * v2
print(resultadov2)

qtdev3= float(input("Digite a quantidade de Tablet que você deseja comprar, se não quiser nenhum, digite 0:"))
resultadov3 = qtdev3 * v3
print(resultadov3)

qtdev4= float(input("Digite a quantidade de PS5 que você deseja comprar, se não quiser nenhum, digite 0:"))
resultadov4 = qtdev4 * v4
print(resultadov4)

qtdev5= float(input("Digite a quantidade de Notebook que você deseja comprar, se não quiser nenhum, digite 0:"))
resultadov5 = qtdev5 * v5
print(resultadov5)

total = resultadov1+resultadov2+resultadov3+resultadov4+resultadov5
print("O valor total da compra de todos os produtos é: ", total)

print("O valor da parcela dividido em 3X sem juros, será: ", total/3)

parcela5 = (total/6) + (0.05*total)
print("O valor da parcela dividido em 6X com acréscimo de 5%, será:", parcela5)

desconto10 = (total*0.1)
print("O valor com 10% de desconto para pagamento à vista, será: ", total-desconto10)


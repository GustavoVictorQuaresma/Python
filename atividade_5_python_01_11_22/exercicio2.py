# Crie um programa que leia um conjunto de nomes de 20 estudantes inscritos na prova do ENEM.
# Com esses nomes, realizar uma ordenação crescente usando uma função para facilitar a localização do nome na lista
# que será afixada no quadro de avisos da escola.

print("Programa Nomes dos estudantes do ENEM")

lista = ["Helena", "Alice", "Laura", "Manuela", "Sophia", "Isabella", "Luísa", "Heloísa", "Cecília", "Maitê", "Eloá", "Elisa", "Liz", "Júlia", "Maria Luísa", "Valentina", "Maria Alice", "Lívia", "Antonella", "Lorena"]
print("Os nomes dos 20 estudantes inscritos na prova do ENEM são: ", lista)

lista.sort()
print("Os nomes em ordem crescente é: ", lista)

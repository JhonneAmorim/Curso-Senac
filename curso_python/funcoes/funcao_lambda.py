# Função lambda em Python
# A função lambda é uma função como qualquer outra em python.
# Porém, são funções anônimas que contém apenas uma linha.. Ou seja,
# tudo deve ser cotido dentro de uma única expressão
# lista = [
#  {'nome': 'Jhonne', 'sobrenome': 'Amorim'},
#  {'nome': 'Jhon', 'sobrenome': 'Costa'},
#  {'nome': 'Joao', 'sobrenome': 'Breno'},
#  {'nome': 'Julio', 'sobrenome': 'Diniz'},
#  {'nome': 'James', 'sobrenome': 'Estevao'},
# ]
#
#
# lista = [4, 34, 5, 1, 6, 21, 10]
# lista.sort()
# # sorted(lista)
# print(lista)

lista = [
 {'nome': 'Jhonne', 'sobrenome': 'Amorim'},
 {'nome': 'Jhon', 'sobrenome': 'Costa'},
 {'nome': 'Joao', 'sobrenome': 'Breno'},
 {'nome': 'Julio', 'sobrenome': 'Diniz'},
 {'nome': 'James', 'sobrenome': 'Estevao'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()
# lista.sort(key=lambda item: item['sobrenome'])
l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])
# for item in lista:
#     print(item)

exibir(l1)
exibir(l2)

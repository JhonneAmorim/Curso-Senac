# Mapeamento de dados em list comprehension
import pprint


def printar(v):
    pprint.pprint(v, sort_dicts=False, width=40)


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto}
                  for produto in produtos]

# print(*novos_produtos, sep='\n')
# pprint.pprint(novos_produtos)
# printar(novos_produtos)

# Filtrando no list comprehension
# O que vem na esquerda do for mapeamento e na direita do for e filtro
lista = [n for n in range(10) if n < 5]
# print(lista)

novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto}
                  for produto in produtos if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10]

printar(novos_produtos)

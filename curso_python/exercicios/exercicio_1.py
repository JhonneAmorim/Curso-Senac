import copy

# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 3', 'preco': 105.87},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 4', 'preco': 69.90},
    {'nome': 'Produto 2', 'preco': 10.11},
]

# Gere novos_produtos por deep coypy (cópia profunda)

novos_produtos = copy.deepcopy(produtos)

novos_produtos.append({'nome': 'Produto 7', 'preco': 29.90})
novos_produtos.append({'nome': 'Produto 8', 'preco': 129.90})
novos_produtos.append({'nome': 'Produto 6', 'preco': 169.90})

print('NOVOS PRODUTOS')
print(novos_produtos)
print()

# Aumente os preços dos produtos a seguir em 10%
print('AUMENTANDO PREÇOS DOS PRODUTOS EM 10%')
aumento = [produto['preco'] + (produto['preco'] * 10 / 100)
           for produto in novos_produtos
           ]
for i in aumento:
    print(f'{i:.2f}')

print()

# Gere produtos_ordernados_por_nome por deep copy (copia prfunda)
# Ordene os produtos por nome descrescente (do maior para menor)
print('PRODUTOS ORDENADOS POR ORDEM DESCRESCENTE')
ordem_dos_produtos = sorted(
    novos_produtos, key=lambda n: n['nome'], reverse=True)
for ordene_prod in ordem_dos_produtos:
    print(ordene_prod)
print()

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# Ordene os produtos por preço crescente (do menor para maior)
print('PREÇO ORDENADOS EM ORDEM CRESCENTE')
ordem_dos_precos = sorted(novos_produtos, key=lambda p: p['preco'])
for ordene_preco in ordem_dos_precos:
    print(ordene_preco)
print()

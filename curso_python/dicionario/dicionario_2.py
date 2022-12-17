# manipulando chaves e valores em dicionarios

pessoa = {}

# pessoa['nome'] = 'Jhonne'

# print(pessoa)
# print(pessoa['nome'])

chave = 'nome'

pessoa[chave] = 'Jhonne'
pessoa['sobrenome'] = 'Amorim'

print(pessoa[chave])

pessoa[chave] = 'Elyzandra'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
  print('não existe')
else:
  print(pessoa['sobrenome'])
  
"""
Dicionarios em Python (tipo dict)
Dicionarios são estruturas de dados do tipo par de "chave" e "valor"
Chaves podem ser consideradas como o "índice" que vimos na lista e pode ser de tipo imutáveis
como : str, int, float, bool, tuple. etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário
Usuamos as cheves - {} - ou a classe dict para criar dicinarios
Imutáveis: str, int, float, bool, tuples
Mutavel: dict, list 
"""

pessoa = {
  'nome': 'Jhonne',
  'sobrenome': 'Amorim Oliveira',
  'idade': 23,
  'altura': 1.76,
  'endereços': [
    {'rua': 'Waldermar ferreira do vale', 'numero': 97},
    {'rua': 'Raimundo Pacheco', 'numero': 288},
  ],
}

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print()

for chave in pessoa:
  print(chave, pessoa[chave])
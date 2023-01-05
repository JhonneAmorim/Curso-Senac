# Exercicio - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizoente']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest

"""
Primeira resposta é formar como consegui resolver o problema
"""
def unir_lista():
    estado = ['BA', 'SP', 'MG', 'RJ']
    cidade = ['Salvador', 'Ubatuba', 'Belo Horizoente']
    lista_unida = list(zip(cidade, estado))
    return lista_unida

print(unir_lista())

"""
Segunda e Terceira resposta é a formar de como aprendir
a resolver o problema de outras maneiras
"""

estado = ['BA', 'SP', 'MG', 'RJ']
cidade = ['Salvador', 'Ubatuba', 'Belo Horizoente']
print(list(zip_longest(cidade, estado, fillvalue='Sem Cidade')))



def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
    ]


estado = ['BA', 'SP', 'MG', 'RJ']
cidade = ['Salvador', 'Ubatuba', 'Belo Horizoente']
print(zipper(cidade, estado))

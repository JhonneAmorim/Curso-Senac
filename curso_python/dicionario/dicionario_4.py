#  Empacotamento e desempacotamento de dicionarios

a, b = 1, 2
a, b = b, a
# print(a, b)

# EMPACOTAMENTO
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chabe, valor in pessoa.items():
#     print(chave, valor)

#DESEMPACOTAMENTO   
pessoa = {
    'nome': 'Alice',
    'sobrenome': 'Vieira',
}

dados_pessoa = {
    'idade': 23,
    'altura': 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)
# empacotando em kwargs
# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# desempacotando em kwargs
mostro_argumentos_nomeados(**pessoa_completa)

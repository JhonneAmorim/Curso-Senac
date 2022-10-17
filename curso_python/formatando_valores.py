

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
#formatando para duas casa decimais
print( '{:.2f}'.format(divisao) )
print(f"{divisao:.2f}")

nome = 'Luiz Otavio'
print(f"{nome:s}")

num_3 = 3
print(f"{num_3:0>10}")

num_4 = 1150
print(f"{num_4:0^10}")
print(f"{num_4:0<10}")
print(f"{num_4:0>10}")
print(f"{num_4:0>10.2f}")

nome = "Otavio miranda"
print(nome.lower()) # tudo minusculo
print(nome.upper()) # tudo maisculo
print(nome.title()) # primeira letra maisculas
print(len('##################'))
print(f"{nome:#^50}")
sobrenome = 'Mario'
nome_formatado = '{0:$^50}{1:#^50}'.format(nome, sobrenome)
print(nome_formatado)
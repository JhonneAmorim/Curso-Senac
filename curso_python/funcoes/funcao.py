def saudacao(msg = 'Olá', nome = 'Usuário'):
  nome = nome.replace('e', '3')
  msg = msg.replace('e', '3')
  # print(msg, nome)
  return f'{msg} {nome}'


variavel = saudacao()
print(variavel)
# saudacao('Olá', 'Jhonne')
# saudacao('Oi', 'Jhon')
# saudacao('Hello', 'João')
# saudacao(nome = 'Zezinho', msg = 'Hi')


def divisao(n1, n2):
  if n2 == 0:
    return
  
  return n1 / n2

divide = divisao(8, 2)
if divide:
  print(divide)
else:
  print('Conta invalida')
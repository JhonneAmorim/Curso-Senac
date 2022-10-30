# 3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex: 10%)
# Retorne (return) o alor do primeiro número somado do aumento do percentual do mesmo.

def somar_de_pencentual(x, y):
  porcentagem = y / 100
  calc_da_porcentagem = x + x * porcentagem 
  return calc_da_porcentagem

print(somar_de_pencentual(100, 10))
print(somar_de_pencentual(50, 10))
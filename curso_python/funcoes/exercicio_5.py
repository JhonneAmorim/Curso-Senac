def multiplicar_numeros(*args):
  total = 1
  for numero in args:
    total *= numero
  return total

multiplicacao = multiplicar_numeros(1, 2, 3, 4, 5)
print(multiplicacao)
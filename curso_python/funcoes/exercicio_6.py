def mostrar_par_impar(num):
  
  if num % 2 == 0:
    return f'número: {num} é par'
  return f'número: {num} é impar'

print(mostrar_par_impar(10))
print(mostrar_par_impar(5))
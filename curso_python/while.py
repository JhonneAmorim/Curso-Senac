frase = input("Digite um frase de sua preferência: ")

tamanho_da_frase = len(frase)

contador = 0

nova_string = ''

input_do_usuario = input("Qual letra desejar colocar maiúscula: ")

while contador < tamanho_da_frase:
  letra = frase[contador]
  if letra == input_do_usuario:
    nova_string += input_do_usuario.upper()
  else:
    nova_string += letra
  contador += 1

print(nova_string)
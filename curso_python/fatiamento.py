# positivos [012345678]
texto = 'Python_s2'
#negativos [-98765421] 

# print(texto[2])
# print(texto[8])
print(len(texto))

for letra in texto:
  print(letra)

# url = 'www.google.com.br/'
# print(url[:-1])

#                   incio e fim
nova_string = texto[2:6]
#                   incio e fim e passo
nova_string = texto[0::2]
print(nova_string)
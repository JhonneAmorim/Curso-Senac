#{key: value}

notas = {
  "alice": 10,
  "bob": 8,
  "carlos": 9
}

print(notas["alice"])
# print(notas["abc"])

janeiro = {
  1: "Sábado",
  2: "Domingo"
}

print(janeiro[1])

alice = {
  "nome": "Alice",
  "idade": 26,
  "admin": False
}

bob = {
  "idade": 26,
  "nome": "Bob",
  "admin": False
}

robson = {
  "nome": "Robson",
  "endereço": {
    "rua": "25 de Março",
    "numero": 278
  } 
}
print(alice["nome"])
print(bob["nome"])

print(robson["nome"])
print(robson["endereço"])
print(robson["endereço"]["rua"])

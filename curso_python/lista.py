# notas = [8, 10, 8.5]
# #        0   1   2
# notas.append(9)
# print(notas)

# #ordena
# notas.sort()
# print(notas)
# notas.sort(reverse=True)
# print(notas)

# # remove o ultimo valor da lista
# x = notas.pop()
# print(notas)
# print("x", x)

# # add valor sem ser no final dela
# notas.insert(0, 8)
# print("apos inserção")
# print(notas)

# # remover o valor de acordo com index
# notas.pop(0)
# print(notas)

#lista heterogena
# pessoa = ["Gabriel", 27, "123123"]

# print("o nome é", pessoa[0])
# print("a idade é", pessoa[1])

# # list dentro de list
# # pode ser uma matriz
# # entre outro tipo de list
# pessoas = [
#   ["Gabriel", 27],
#   ["Jhonne", 22],
# ]
# matriz = [
#   [20, 10],
#   [10, 20]
# ]

notas = [8, 9, 10, 7.5, 4, 6]

i = 0
total = 0

qtd = len(notas)
while i < qtd:
  total = total + notas[i] 
  i = i + 1

print("O total das notas é: ", total)
media = total / qtd
print("A media das notas  é: ", media)

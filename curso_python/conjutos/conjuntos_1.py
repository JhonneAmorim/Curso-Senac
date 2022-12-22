# Sets- Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama de Venn
#Sets em Python são mutáveis, porém aceitam apenas tipo imutáveis como valor interno
#
#Criando um set
# set(iterável) ou {1, 2 ,3}
# s1 = set() vazio
# s1 = {'Jhonne', 1, 2, 3} # com dados
# print(s1, type(s1))
#
#Sets são eficientes para remover valores duplicados de iteráveis
# eles não tem índexes
# eles não garatem ordem
# eles são iteráveis (for, in, not in)
# l1 = [1, 2, 3, 3, 3, 3, 3]
# s1 = set(l1)
# l2 = list(s1)
# s1 = set('Jhonne')
# s1 = {1, 2, 3, (123,)}
# s1 = {1, 2, 3}
# print(3 in s1)
# for numero in s1:
#     print(numero)
#
# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Jhonne')
# s1.add(1)
# s1.update(('Ola Mundo', 4, 5, 6, 7))
# # s1.clear()
# s1.discard('Ola Mundo')
# s1.discard('Jhonne')
# print(s1)
#
# Operadores úteis:
# união | união (union) - Une
# Intersecção & (intersersection) Itens presente em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ Itens que não estão em ambos
#
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)

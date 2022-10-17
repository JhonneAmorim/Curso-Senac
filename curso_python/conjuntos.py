usuarios = set(["alice", "bob", "alice"])
usuarios_2 = set(["alice", "lucas", "joão"])

# print(usuarios == usuarios_2)

#conjutos não possuem elementos repetidos
# print(usuarios)
# usuarios.add("bob")
# print(usuarios)
# usuarios.add("carlos")
# print(usuarios)

# removendo duplicadas de uma lista
# usuarios_unicos = set(usuarios)
# print(usuarios_unicos)

#conjutos de união
# operador do union = |
print(usuarios.union(usuarios_2))
print(usuarios | usuarios_2)

#interseção
print(usuarios.intersection(usuarios_2))
print(usuarios & usuarios_2)

#diferença
print(usuarios.difference(usuarios_2))
print(usuarios - usuarios_2)
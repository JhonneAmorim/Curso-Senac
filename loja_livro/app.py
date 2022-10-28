from livro import Livro
from dvd import DVD
from cd import CD

livro = Livro("nome", 0.99, "autor")
dvd = DVD("nome", 0.99, "1:16:39")
cd = CD("nome", 0.99, 5)

print(livro.mostrar_livros())
print(dvd.mostrar_dvds())
print(cd.mostrar_cds())


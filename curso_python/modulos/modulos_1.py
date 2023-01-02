# Módulos padrão do Python (import, from, as e *)
# inteiro - import nome_modulo
# Vantagens : você tem o namespace do módulo
# Desvantagens: nome grandes
# import sys

# platfom = "A Minha"
# print(sys.platform)
# print(platfom)
#
# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform
#
# print(platform)

# alias 1 import nome_modulo as apelido
# import sys as s

# sys = 'Alguma coisa'
# print(s.platform)
# print(sys)

# alias 2 from nome_moduli import objeto as apleido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: voce pode reservar nomes para seu codigo
# Desvantagens: pode ficar fora do padrão da linguagem
#
# má pratica from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import *

print(platform)
exit()

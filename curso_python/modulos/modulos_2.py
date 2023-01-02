# Entendendo os seus príprios módulos Python
# O primeiro módulo executado chama-se __main__
# VocÊ pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O Python conhece todos os módulos e pacotes presente nos caminhos de sys.path
# import sy

import modulos_2_m
from modulos_2_m import somar, variavel_nome

# print('Este módulo se chama', __name__)
# print(*sys.path, sep='\n')
print(modulos_2_m.variavel_nome)
print(variavel_nome)
print(somar(2, 3))
print(modulos_2_m.somar(2, 3))

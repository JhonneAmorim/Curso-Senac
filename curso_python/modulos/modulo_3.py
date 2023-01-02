import importlib

import modulo_3_m

print(modulo_3_m.variavel)

for i in range(10):
    importlib.reload(modulo_3_m)
    print(i)

print('Fim')

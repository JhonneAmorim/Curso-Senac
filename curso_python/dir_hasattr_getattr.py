# dir, hasattr e getattr em python

string = 'Jhonne'
metodo = 'upper'
# print(dir(string))

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)

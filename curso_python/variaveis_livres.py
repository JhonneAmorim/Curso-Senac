# Variáveis livres + nonlocal (locals, globals)


def concatenar(string_incial):
    valor_final = string_incial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('o')
print(c('k'))
print(c('a'))
print(c('y'))

final = c()
print(final)
# Exercício - Adiando execução de funcões

def somar(x, y):
    return x + y


def multiplicar(x, y):
    return x * y


def executar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna


soma_com_cinco = executar_funcao(somar, 5)
multiplica_por_dez = executar_funcao(multiplicar, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))

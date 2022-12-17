# Exercícios
# Crie funçoes que duplicam, triplicam e quadruplicam
# o número recebido como parâmentro

def criar_multiplicar(multiplicador):
  def multiplicar(numero):
    return numero * multiplicador
  return multiplicar

duplicar = criar_multiplicar(2)
triplicar = criar_multiplicar(3)
quadruplicar = criar_multiplicar(4)

print(duplicar(2), triplicar(2), quadruplicar(2))
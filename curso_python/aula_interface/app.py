from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangulo import TerrenoRetangulo
from engenheiros import Engenheiros

engenheiro = Engenheiros('Fulano')
terreno_quadrado = TerrenoQuadrado(4)
terreno_retangulo = TerrenoRetangulo(2, 3)

engenheiro.medir_area(terreno_quadrado)
engenheiro.medir_perimetro(terreno_quadrado)

print()

engenheiro.medir_area(terreno_retangulo)
engenheiro.medir_perimetro(terreno_retangulo)
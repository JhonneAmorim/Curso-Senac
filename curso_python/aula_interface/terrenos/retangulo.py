from interfaces.formas import IFormas

class TerrenoRetangulo(IFormas):
  def __init__(self, lagura: int, altura: int) -> None:
    self.lagura = lagura
    self.altura = altura

  def get_area(self) -> int:
    area = self.lagura * self.altura
    return area

  def get_perimetro(self) -> int:
    perimetro = (self.lagura * 2) + (self.altura * 2)
    return perimetro
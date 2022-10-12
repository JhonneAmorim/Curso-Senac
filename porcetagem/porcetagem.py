class PorcetagemDeJuros:
  def __init__(self):
    juros = 0

  def calcular_porcetagem(self):

    juros1 = 15 / 100
    juros2 = 25 / 100
    juros3 = 40 / 100
    juros4 = 8 / 100
    juros5 = 9 / 100

    calculo_de_juros1 = self.juros * juros1
    calculo_de_juros2 = self.juros * juros2
    calculo_de_juros3 = self.juros * juros3
    calculo_de_juros4 = self.juros * juros4
    calculo_de_juros5 = self.juros * juros5

    print(f"O valor {self.juros} somado com juros de 15% é igual a: {calculo_de_juros1}")
    print(f"O valor {self.juros} somado com juros de 25% é igual a: {calculo_de_juros2}")
    print(f"O valor {self.juros} somado com juros de 40% é igual a: {calculo_de_juros3}")
    print(f"O valor {self.juros} somado com juros de 8% é igual a: {calculo_de_juros4}")
    print(f"O valor {self.juros} somado com juros de 9% é igual a: {calculo_de_juros5}")
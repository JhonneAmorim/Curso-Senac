# termo geral PG: An = a1 * q ** (n - 1)
# somar termos PG: Sn = (a1 * ((q ** n) - 1)) / q - 1

class ProgressaoGeometrica:

  def __init__(self):
    an = 0
    sn = 0

  def termo_geral_pg(self):
    a1 = int(input("Digite o primeiro termo: "))
    q = int(input("Digite a razão: "))
    tam = int(input("Quantos elementos exibir: ")) 
        
    for n in range(1, tam + 1):
      self.an = a1 * q ** (n - 1)
      self.sn = a1 * (q ** n - 1) / (q - 1)
      print(f"O valor termo geral da pg é: {self.an}")
    print(f"O valor da soma termo geral da pg é: {self.sn}")
    print("")
    
    a1 = int(input("Digite o primeiro termo: "))
    q = int(input("Digite a razão: "))
    tam = int(input("Quantos elementos exibir: ")) 
        
    for n in range(1, tam + 1):
      self.an = a1 * q ** (n - 1)
      self.sn = a1 * (q ** n - 1) / (q - 1)
      print(f"O valor termo geral da pg é: {self.an}")
    print(f"O valor da soma termo geral da pg é: {self.sn}")
    print("")
    
    a1 = int(input("Digite o primeiro termo: "))
    q = int(input("Digite a razão: "))
    tam = int(input("Quantos elementos exibir: ")) 
        
    for n in range(1, tam + 1):
      self.an = a1 * q ** (n - 1)
      self.sn = a1 * (q ** n - 1) / (q - 1)
      print(f"O valor termo geral da pg é: {self.an}")
    print(f"O valor da soma termo geral da pg é: {self.sn}")
    print("")
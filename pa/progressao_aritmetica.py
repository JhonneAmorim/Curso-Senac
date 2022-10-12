# termo geral PA: An = a1 + ((n - 1) * r)
# somar termos PA: Sn = ((a1 + an) * n) / 2

class ProgressaoAritmetica:

  def __init__(self):
    an = 0
    sn = 0

  def termo_geral_pa(self):
    a1 = int(input("Digite o primeiro termo: "))
    r = int(input("Digite a razão: "))
    n = int(input("Quantos elementos exibir: ")) 
    an = a1 + (n-1)*r
    sn = ((a1 + an) * n) / 2
    self.an = an + 1
    self.sn = sn
    for self.an in range(a1, self.an, r):      
      print(f"O valor do termo geral da pa: {self.an}")
    print(f"O valor da soma dos termos da pa: {self.sn}")
    print('')
    
    a1 = int(input("Digite o primeiro termo: "))
    r = int(input("Digite a razão: "))
    n = int(input("Quantos elementos exibir: ")) 
    an = a1 + (n-1)*r
    sn = ((a1 + an) * n) / 2
    self.an = an + 1
    self.sn = sn
    for self.an in range(a1, self.an, r):      
      print(f"O valor do termo geral da pa: {self.an}")
    print(f"O valor da soma dos termos da pa: {self.sn}")
    print('')
    
    a1 = int(input("Digite o primeiro termo: "))
    r = int(input("Digite a razão: "))
    n = int(input("Quantos elementos exibir: ")) 
    an = a1 + (n-1)*r
    sn = ((a1 + an) * n) / 2
    self.an = an + 1
    self.sn = sn
    for self.an in range(a1, self.an, r):      
      print(f"O valor do termo geral da pa: {self.an}")
    print(f"O valor da soma dos termos da pa: {self.sn}")
    print('')
   
from funçao_de_conta import FuncaoDeConta

class ContaEspecial(FuncaoDeConta):

  def __init__(self, saldo, taxa):
    self.saldo = saldo
    self.taxa = taxa
  

  def get_taxa(self):
    return self.taxa

  def set_taxa(self, taxa):
    self.taxa = taxa
  
  def get_saldo(self):
    return self.saldo

  def set_saldo(self, saldo):
    self.saldo = saldo

  def obter_saldo(self):
    return self.get_saldo()

  def depositar(self):
    opcao = ''
    while opcao != "N":
        deposito = int(input("Digite o valor do seu deposito: "))
        self.saldo = self.get_saldo() + deposito
        opcao = input("Desejar fazer um novo depostio: S/N?")                        
    return self.get_saldo()

  def sacar(self):
    opcao = ''
    while opcao != "N":
      saque = int(input("Digite o valor do seu saque: "))
      self.saldo = self.get_saldo() - (saque + saque * self.get_taxa())
      opcao = input("Desejar fazer um novo saque: S/N?") 
    return self.get_saldo()

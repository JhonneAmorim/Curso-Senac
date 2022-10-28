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

  def depositar(self, deposito):
    self.saldo = self.get_saldo() + deposito
    return self.get_saldo()

  def sacar(self, saque):
    self.saldo = self.get_saldo() - (saque * self.get_taxa())
    return self.get_saldo()

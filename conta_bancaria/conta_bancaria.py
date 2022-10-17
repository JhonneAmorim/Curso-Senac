class ContaBancaria:

  def __init__(self, saldo):
    self.saldo = saldo

  def depositar(self, deposito):
    
    self.saldo = self.saldo + deposito
    return self.saldo

  def sacar(self, saque):
    
    self.saldo = self.saldo - saque
    return self.saldo

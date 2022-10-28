from abc import ABC, abstractclassmethod

class FuncaoDeConta(ABC):

  @abstractclassmethod
  def obter_saldo(self):
    ...
    
  @abstractclassmethod
  def depositar(self):
    ...

  @abstractclassmethod
  def sacar(self):
    ...

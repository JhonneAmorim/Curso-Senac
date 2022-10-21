class Pessoa:
  def __init__(self, nome, data_nasc, altura):
    self.__nome = nome
    self.__data_nasc = data_nasc
    self.__altura = altura

  def get_nome(self):
    return self.__nome
  
  def set_nome(self, nome):
    self.__nome = nome

  def get_data_nasc(self):
    return self.__data_nasc
  
  def set_data_nasc(self, data_nasc):
    self.__data_nasc = data_nasc

  def get_altura(self):
    return self.__altura
  
  def set_altura(self, altura):
    self.__altura = altura

  def calcular_idade(self):
    idade = 2022 - self.get_data_nasc()
    return idade

  def dados_da_pessoa(self):
    print("Nome: ", self.get_nome())
    print("idade: ", self.calcular_idade())
    print("altura: ", self.get_altura())
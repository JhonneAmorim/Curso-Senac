from conta_bancaria import ContaBancaria

saldo_da_conta = ContaBancaria(1000)


class Pessoa:

  def __init__(self, nome, idade, endereco, profissao):
    self.nome = nome
    self.idade = idade
    self.endereco = endereco
    self.profissao = profissao

  def receber_salario(self):
    salario_a_receber = print(f"Depositor de salario feito com sucesso, {saldo_da_conta.depositar(2500)}")
    
  def retirar_salario(self):
    salario_a_retirar = print(f"Sacar dinheiro da minha conta, {saldo_da_conta.sacar(1800)}")

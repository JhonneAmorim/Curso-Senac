from conta_corrente import ContaCorrente
from conta_especiais import ContaEspecial 

c_corrente = ContaCorrente(1000, 0.05)
c_especial = ContaEspecial(4500, 0.01)


c_corrente.depositar()
c_corrente.sacar()
print("Seu saldo da conta corrente é:",c_corrente.obter_saldo())

print()

c_especial.depositar()
c_especial.sacar()
print("Seu saldo da conta especial é:",c_especial.obter_saldo())

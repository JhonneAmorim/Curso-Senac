from fractions import Fraction

class divisoesNumerica:
  def __init__(self):
    a = 0
    b = 0

  def dividir_num(self):
    a = float(input("Digite um numero A: "))
    b = float(input("Digite um numero B: "))

    print(f"O resto da divisão {a % b}")
    print(f"O valor exato da divisão {a / b}")
    print(f"A parte inteira da divisão {a // b}")
    print(f"A parte fracionária da divisão {Fraction(a / b)}")
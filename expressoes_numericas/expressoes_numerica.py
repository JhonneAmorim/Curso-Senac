# (self.x *( 4 + self.y)*(10 - self.x)) ** 2 / (self.x - self.y)
# ((3 ** 8) / self.y) + ((10 * self.x + (8 ** 8) + 90 * self.y) / 1000) - 88 / ( self.x * self.y)

class ExpressoesNumericas:
    def __init__(self):
        x = 0
        y = 0

    def calcular_expressoes1(self):
        self.x = int(input("Digite um numero: "))
        self.y = int(input("Digite um numero: "))

        print(
            f"O resultado da expressão numerica é:{(self.x *( 4 + self.y)*(10 - self.x)) ** 2 / (self.x - self.y)}")

    def calcular_expressoes2(self):
        self.x = int(input("Digite um numero: "))
        self.y = int(input("Digite um numero: "))

        print(
            f"O resultado da expressão numerica é:{((3 ** 8) / self.y) + ((10 * self.x + (8 ** 8) + 90 * self.y) / 1000) - 88 / ( self.x * self.y)}")

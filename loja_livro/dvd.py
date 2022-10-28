from loja import ILoja

class DVD(ILoja):
    def __init__(self, nome, preco, duracao):
        self.nome = nome 
        self.preco = preco 
        self.duracao = duracao
        

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome 
        
    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco 

    def get_duracao(self):
        return self.duracao

    def set_duracao(self, duracao):
        self.duracao = duracao

    def mostrar_arquivos(self):
        self.set_nome(input("Digite seu nome do dvd: "))
        self.set_preco(float(input("Digite o preço: ")))
        self.set_duracao(input("Digite a duracao do dvd: "))

        vetor = [self.get_nome(), self.get_preco(), self.get_duracao()]
        return vetor

    def mostrar_dvds(self):
        dvd = []
        for i in range(5):
            dvd.append(self.mostrar_arquivos())
        return dvd
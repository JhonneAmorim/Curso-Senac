from loja import ILoja

class CD(ILoja):
    def __init__(self, nome, preco, faixas):
        self.nome = nome 
        self.preco = preco 
        self.faixas = faixas
        

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome 
        
    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco 

    def get_faixas(self):
        return self.faixas

    def set_faixas(self, faixas):
        self.faixas = faixas

    def mostrar_arquivos(self):
        self.set_nome(input("Digite seu nome do cd: "))
        self.set_preco(float(input("Digite o preço: ")))
        self.set_faixas(int(input("Digite a faixas do cd: ")))

        vetor = [self.get_nome(), self.get_preco(), self.get_faixas()]
        return vetor

    def mostrar_cds(self):
        cd = []
        for i in range(5):
            cd.append(self.mostrar_arquivos())
        return cd
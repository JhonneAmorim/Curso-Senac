from loja import ILoja

class Livro(ILoja):
    def __init__(self, nome, preco, autor):
        self.nome = nome 
        self.preco = preco 
        self.autor = autor       

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome 
        
    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco 

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def mostrar_arquivos(self):
        self.set_nome(input("Digite seu nome: "))
        self.set_preco(float(input("Digite o preço: ")))
        self.set_autor(input("Digite seu nome do autor: "))

        vetor = [self.get_nome(), self.get_preco(), self.get_autor()]
        return vetor

    def mostrar_livros(self):
        livro = []
        for i in range(5):
            livro.append(self.mostrar_arquivos())
        return livro

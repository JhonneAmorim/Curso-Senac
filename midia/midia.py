class Midia:
    def __init__(self, codigo, preco, nome, tipo, detalhes, print_dados, inserir_dados):
        self.__codigo = codigo
        self.__preco = preco
        self.__nome = nome
        self.tipo = tipo
        self.detalhes = detalhes
        self.print_dados = print_dados
        self.inserir_dados = inserir_dados

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_tipo(self) -> str:
        return self.tipo

    def set_tipo(self, tipo) -> str:
        self.tipo = tipo

    def get_detalhes(self) -> str:
        return self.detalhes

    def set_detalhes(self, detalhes) -> str:
        self.detalhes = detalhes

    def get_print_dados(self):
        return self.print_dados

    def set_print_dados(self, print_dados):
        self.print_dados = print_dados

    def get_inserir_dados(self):
        return self.inserir_dados

    def set_inserir_dados(self, inserir_dados):
        self.inserir_dados = inserir_dados

    def midia(c = int, p = float, f = int):
        c = 10 
        p = 15.5 
        f = 20
        print('numero da midia c: ', c)
        print('minuto da midia: ', p)
        print('numero da mida f: ', f)
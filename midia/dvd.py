from midia import Midia


class DVD(Midia):
    def __init__(self, codigo, preco, nome, tipo, detalhes, print_dados, inserir_dados, nFaixas, faixas):
        self.__nFaixas = nFaixas
        self.faixas = faixas
        super().__init__(codigo, preco, nome, tipo, detalhes, print_dados, inserir_dados)

    def get_nFaixas(self):
        return self.__nFaixas

    def set_nFaixas(self, nFaixas):
        self.__nFaixas = nFaixas

    def get_faixas(self):
        return self.faixas

    def set_faixas(self, faixas):
        self.faixas = faixas


    def dvd(c = int, p = float, f = int, s = str):
        c = 2 
        p = 15.5 
        f = 20
        s = "Nome do filme é esse"
        print('numero do filme : ', c)
        print('minuto do filme: ', p)
        print('numero de visualização : ', f)
        print('nome do dvd: ', s)
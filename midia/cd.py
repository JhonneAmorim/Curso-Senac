from midia import Midia

class CD(Midia):
    def __init__(self, codigo, preco, nome, tipo, detalhes, print_dados, inserir_dados, nMusicas, musica):
        self.__nMusicas = nMusicas
        self.musica = musica
        super().__init__(codigo, preco, nome, tipo, detalhes, print_dados, inserir_dados)

    def get_nMusicas(self):
        return self.__nMusicas

    def set_nMusicas(self, nMusicas):
        self.__nMusicas = nMusicas

    def get_musica(self):
        return self.musica

    def set_musica(self, musica):
        self.musica = musica


    def cd(c = int, p = float, m = int, s = str):
        c = 10 
        p = 30.59 
        m = 190
        s = "Nome da musica"
        print('numero da faixa c: ', c)
        print('minuto do cd: ', p)
        print('minuto da faixa f: ', m)
        print('Cd musica tal....: ', s)
from abc import ABC, abstractclassmethod

class ILoja(ABC):

    @abstractclassmethod
    def mostrar_arquivos(self):
        pass
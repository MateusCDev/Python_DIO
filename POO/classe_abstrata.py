from abc import ABC, abstractmethod, abstractproperty # importando o modulo ABC

# Interface
class ControleRemoto(ABC): # extendendo do modulo ABC
    
    #metodos abstratos
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod    
    def desligar(self):
        pass

    @property #implementando um metodo de propriedade na interface
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):

    #implementando os metodos abstratos na classe que extendeu da classe abstrata  pois se tornar obrigatorio a implementação

    def ligar(self):
        print("ligando a TV...")
        print("Tv ligada")

    def desligar(self):
        print("Desligando a Tv..") 
        print("Tv desligada") 

    @property
    def marca(self):
        return "Sony"    

class ControleArCondicionado(ControleRemoto):

    def ligar(self):
        print("ligando o Ar...")
        print("Ar ligado")

    def desligar(self):
        print("Desligando o Ar..") 
        print("Ar desligado") 

    @property
    def marca(self):
        return "Consul"




controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)


controle= ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
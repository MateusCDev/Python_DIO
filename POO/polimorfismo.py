class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar() #executando o metodo da classe pai chamando a função super()
        print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

# FIXME: exemplo ruim do uso de herança para "ganhar" o metodo voar
class Aviao(Passaro):
    def voar(self):
        print("Avião esta decolando ...")        


def plano_de_voo(obj): # um metodo declarado fora do escopo chamando qualquer um dos metodos voar de ambas classes
    obj.voar()

# polimorfismo sendo aplicado
plano_de_voo(Pardal()) 
plano_de_voo(Avestruz()) 
plano_de_voo(Aviao())   
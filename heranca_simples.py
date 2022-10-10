class Veiculo:
    def __init__(self, cor, placa, numero_rodas, motor = False):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        self.motor = motor

    def ligar_motor(self):
        if self.motor == False:
            print("Ligando o motor")
            
    def desligar_motor(self):
        if self.motor == True:
            print("Desligando motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado = False, **kw):
        super().__init__(**kw)
        self.carregado = carregado

    def esta_carregado(self):
        if  self.carregado == False:
            print("Não estou carregado")
        else:
            print("Esta carregado")    

moto= Motocicleta(cor="preto", placa="RPG-1234", numero_rodas=2)
moto.ligar_motor()

carro = Carro(cor="branco", placa="JJL-5211", numero_rodas=4)
carro.ligar_motor()

caminhao = Caminhao(cor="azul", placa="ZJI-0225", numero_rodas=8)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(f"""{caminhao}, 
{carro}, 
{moto}""")
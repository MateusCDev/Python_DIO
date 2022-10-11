class Gato:
    def __init__(self, nome, cor, acordado = True): #Executado no inicio da instacia do objeto
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def miar(self):
        print("miau")

    def acordar(self):
        if self.acordar == False:
            self.acordado = True
            print(f"{self.nome} Acordando") 

    def dormindo(self):
        if self.acordar == True:
            self.acordar == False
            print(f"{self.nome} esta dormindo")

    def __del__(self): # Destroi a instancia liberando memoria 
        print("removendo a instância da classe ...")            

gato1 = Gato("Thor", "Caramelo")

gato1.miar()

print(gato1.nome)



       
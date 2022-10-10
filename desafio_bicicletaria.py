class Bicicleta:
    def __init__(self, cor, modelo, ano ,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1

    def buzinar(self): 
        print("Plim Plim!")  

    def parar(self):
        print("Parando bicicleta ....")   
        print("Bicicleta parada!")

    def correr(self):
        print("shaaaaaa ...")

    def troca_marcha(self, n_marcha):
        print("Troncando a marcha")

        if n_marcha > self.marcha:
            print(f"Marcha trocada na marcha {n_marcha}")
        else:
            print("Não foi possivel trocar de marcha...")        

    # Acessando o nome da classe e seus atributos com o str
    #def __str__(self):
       # return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"   
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("azul", "caloi", 2022, 1200) 

b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("amarelo", "monark", 2019, 900)
b2.buzinar #Bicicleta.buzinar(b2) equivalente

b2.troca_marcha(5)

print(b2)
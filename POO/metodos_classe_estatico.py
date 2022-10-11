class Pessoa:
    def __init__(self, nome=None , idade= None) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod # transformar em um metodo de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade) 

    @staticmethod # metodo estatico
    def e_maior_idade(idade):
        if idade >= 18:
            return  "É maior de idade"  
        else:
            return  "Não é maior de idade"       
    
#p= Pessoa("Mateus", 23)
#print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1998, 12, 25, "Mateus")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(23))
print(Pessoa.e_maior_idade(13))


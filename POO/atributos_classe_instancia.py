class Estudante:
    #atributos de classe são compartilhados em varios objetos então influencia em todos criados
    escola = "DIO"

    # atributos de instancia são unicos para cada objeto criado por isso não influencia em outro objeto
    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)    


aluno_1 = Estudante("Mateus", 1 )
aluno_2 = Estudante("Gessica", 2)
mostrar_valores(aluno_1, aluno_2)


Estudante.escola = "Python" # altera o valor pra todos os objetos
aluno_3 = Estudante("Araujo", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
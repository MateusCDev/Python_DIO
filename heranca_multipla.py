class Animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Onitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, n_patas):
        print(Onitorrinco.__mro__) # mostra a ordem em que a instancia busca os metodos
        print(Onitorrinco.mro()) # Funciona igual a de cima como metodo
        
        super().__init__(cor_pelo = cor_pelo, cor_bico=cor_bico, n_patas=n_patas)



gato = Gato(n_patas=4, cor_pelo="Branco")
print(gato)

onitorrinco = Onitorrinco(n_patas =2, cor_pelo="Marrom", cor_bico="laranja")
print(onitorrinco)
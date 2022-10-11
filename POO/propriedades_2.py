class Pessoa:
    def __init__(self, nome , ano_nascimento) -> None:
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property # seria um get
    def idade(self): # propiedade computada é um atributo que passa uma função
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento



pessoa = Pessoa("Mateus", 1998)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
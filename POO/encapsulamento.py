class Conta:
    def __init__(self,n_agencia, saldo =0):
        self._saldo = saldo # variavel de recurso privado pois por convenção esta utilizando "_"
        self.n_agencia = n_agencia
        
    def depositar(self, valor):
        self._saldo += valor
        pass    

    def sacar(self,valor):
        self._saldo -= valor
        pass
    
    def mostrar_saldo(self): # forma correta de mostrar o atributo privado atravez de um metodo
        return self._saldo


conta = Conta("0200",100) # forma errada pois o atributo da classe é privada
conta.depositar(100) # forma correta de manipular o valor utilizando o metodo pois ele é publico   
print(conta.n_agencia, conta.mostrar_saldo())
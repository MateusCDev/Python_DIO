from abc import ABC, abstractclassmethod, abstractproperty
#Sistema Bancario V3

class Cliente:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)            

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco) -> None:
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente) -> None:
        self._saldo=0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero      

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico     

    def saque(self, valor):
        saldo = self.saldo

        if (valor <= saldo): 
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Operação não realizada! Valor invalido!")
            return False
 
        

    def deposito(self, valor):
        
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado!")
            
        else:
            print("Operação falhou! Valor invalido!")
            return False 

        return True     

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, LIMITE_SAQUES=3) -> None:
        super().__init__(numero, cliente)
        self._limite = limite
        self._LIMITE_SAQUES = LIMITE_SAQUES

    def saque(self, valor):
        numero_saques = len(
            [transacao for transacao in self._historico.
            transacoes if transacao['tipo']== Saque.__name__]
        )    

        if numero_saques >= self._LIMITE_SAQUES:
            print("A quantidade de saques excedeu o limite diario ")    

        elif valor > self._limite:
            print("O valor excede o limite")

        else:
            return super().saque(valor)    

        return False  

    def __str__(self):
        return f"""
                Agencia:{self._agencia}
                NºConta:{self._numero}
                Titular:{self._cliente.nome}
                """      

class Historico:

    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes 

    def incluir_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor
            }
        )       

class Transacao(ABC):
    
    @property
    @abstractproperty
    def valor(self):
        pass


    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor 

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):

        if conta.saque(self.valor):
            conta._historico.incluir_transacao(self)       

class Deposito(Transacao):

    def __init__(self, valor) -> None:
        self._valor = valor 

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):

        if conta.deposito(self.valor):
            conta._historico.incluir_transacao(self)        


def menu():
    menu = """

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Novo usuario
        [5] Nova conta
        [6] Listar contas
        [0] Sair

        => """
    return int(input(menu))  


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(" Cliente não possui conta!")
        return

    #  não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n********* EXTRATO *********")
    transacoes = conta._historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta._saldo:.2f}")
    print("****************************************")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(" Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print(" Cliente criado com sucesso!")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(" Cliente não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(" Conta criada com sucesso! ")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(str(conta))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            depositar(clientes)

        elif opcao == 2:
            sacar(clientes)

        elif opcao == 3:
            exibir_extrato(clientes)

        elif opcao ==  4:
            criar_cliente(clientes)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()            
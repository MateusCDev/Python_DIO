# Sistema bancario

# Funções
def menu():
    menu = """

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Novo usuario
        [5] Nova conta
        [0] Sair

        => """
    return int(input(menu))    

def saque(*,saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

        valor = float(valor)
        
        if (valor <= saldo) and (numero_saques < LIMITE_SAQUES) and (valor < limite):
            numero_saques += 1
            saldo -= valor
            extrato += f'-Saque: R${valor:.2f}\n'
        
        elif valor > saldo:
            print("Sem saldo suficiente")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("A quantidade de saques excedeu o limite diario ") 
        
        elif  valor > limite:
            print("O valor excede o limite")

        return saldo, extrato     

def depositar(saldo, valor, extrato,/):

        if valor > 0:
            saldo += valor
            extrato += f'\n-Deposito: R${valor:.2f}\n'
            
        else:
            print("Operação falhou! Valor invalido!")

        return saldo, extrato     

def exibir_extrato(saldo, /,*,extrato):
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f""" **EXTRATO:
            {extrato}
            -Saldo total: R${saldo}
            ************************
            """
            )

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente Numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario == True:
        print("\n Existe usuario com este CPF! ")
        return
    else:    
        nome = str(input("Informe o nome completo: "))
        data_nascimento = str(input("Informe a data de nascimento (dd/mm/aaaa): ")) 
        endereco = str(input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "))

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}) 

        print("Usuário criado!") 

def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input("Informe o CPF do usuario"))
    usuario= filtrar_usuario(cpf, usuarios)

    if usuario == True:
        print("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuario não encontrado, criação de conta encerrado!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None

def main():

    
    saldo = 0
    limite =500
    extrato = ""
    numero_saques= 0
    numero_conta = 0

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []
        
    while True:

        opcao = (menu())

        #Deposito
        if opcao == 1:

            valor_deposito = float(input("Digite o valor para deposito: "))
            
            saldo, extrato = depositar(saldo,valor_deposito,extrato)
        
        #Saque
        elif opcao == 2:

            valor_saque = float(input("Digite o valor que deseja sacar: "))
            
            saldo, extrato = saque(
                saldo=saldo, 
                valor=valor_saque,
                extrato=extrato, 
                limite=limite,
                numero_saques=numero_saques, 
                LIMITE_SAQUES=LIMITE_SAQUES
                )

        #Extrato         
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
        
        #Criando Usuario
        elif opcao == 4:
            criar_usuario(usuarios)
        
        #Criando conta
        elif opcao == 5:
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
        
        #Sair
        elif opcao == 0:
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

#Função principal sendo chamada
main()            
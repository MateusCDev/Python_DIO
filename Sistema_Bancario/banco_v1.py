menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite =500
extrato = ""
numero_saques= 0
LIMITE_SAQUES = 3


while True:

    opcao = int(input(menu))

    #Deposito
    if opcao == 1:
        valor_deposito = float(input("Digite o valor para deposito: "))
        
        if valor_deposito > 0:
            saldo = valor_deposito
            extrato += f'\n-Deposito: R${valor_deposito:.2f}\n'
        
        else:
            print("Operação falhou! Valor invalido!")    
    #Saque
    elif opcao == 2:
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        
        if (valor_saque <= saldo) and (numero_saques < LIMITE_SAQUES) and (valor_saque < limite):
            saldo -= valor_saque
            numero_saques += 1
            extrato += f'-Saque: R${valor_saque:.2f}\n'
        
        elif valor_saque > saldo:
            print("Sem saldo suficiente")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("A quantidade de saques excedeu o limite diario ") 
        
        elif  valor_saque > limite:
            print("O valor excede o limite")
    #Extrato         
    elif opcao == 3:
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f""" **EXTRATO:
        {extrato}
         -Saldo total: R${saldo}
         ************************
        """)
    #Sair
    elif opcao == 0:
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
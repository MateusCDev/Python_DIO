#if, if else, if elif else

MAIOR_IDADE = 18
IDADE_ESPECIAL = 16


idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode fazer as aulas praticas")
else: 
    print("Ainda não pode tirar a CNH.")

#if aninhado

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!") 
    else:
        print("Não foi possivel realizar o saque, saldo insuficiente!")      
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")    
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.") 

#if ternario
status = "Sucesso" if saldo >= saque else "falha"

print (f"{status} ao realizar o saque!")
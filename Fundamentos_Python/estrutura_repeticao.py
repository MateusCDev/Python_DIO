#for
texto = input("informe um texto: ")
VOGAIS = "AEIOU"

#exemplo usando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:        
    print()  #quebra de linha      

#exemplo utilizando a função built-in range
for  numero in range(0,51,5):
    print(numero, end = " ") 
    print() 

#While

opcao = -1

while opcao != 0:
    opcao = int(input(" [1] Sacar \n [2] Extrato \n [0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibino o extrato ...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")


while True:

    numero = int(input("Digite um numero: "))

    if numero == 10:
        break
    if numero % 2 == 0:
        continue    
    
    print(numero)
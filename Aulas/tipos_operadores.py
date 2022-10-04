produto_1 = 20
produto_2 = 10

# operadores aritimeticos
print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

# operadores de comparação
print(produto_1 > produto_2)
print(produto_1 >= produto_2)
print(produto_1 < produto_2)
print(produto_1 <= produto_2)
print(produto_1 != produto_2)
print(produto_1 == produto_2)

# operadores de atribuição
valor = 30
print(valor)
valor += 30
print(valor)
valor -= 30
print(valor)
valor *= 30
print(valor)
valor /= 30
print(valor)

# operadores logicos
saldo = 1000
saque = 250
limite = 200
conta_especial = True

print((saldo >= saque and saque <= limite)
      or (conta_especial and saldo >= saque))
print(not ((saldo >= saque and saque <= limite)
      or (conta_especial and saldo >= saque)))

# operadores de identidade
saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)

# operadores de associação
frutas = ["limão", "uva"]
nome = "Mateus Cesar de Araujo"

print("laranja" in frutas)
print("limão" not in frutas)
print("Cesar" in nome)


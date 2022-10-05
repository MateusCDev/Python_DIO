#Tuplas são imutaveis e são estruturados dentro de () obs: sempre colocar uma virgula final para identificar uma tupla
frutas = ("limão", "uva", "jaca",)
print(frutas)
letras = tuple("python")
print(letras)
numeros = tuple([1,2,3,4])
print(numeros)

#Acessar o valor na tupla
print(frutas[0])

#Fatiamento na tupla
print(letras[0:2])
print(letras[::-1])

#Tuplas não podem ser alteradas por serem imutaveis

#Count na tupla conta quantas vezes tem o elemento na tupla
print(frutas.count("jaca"))

#Index na tupla mostra a posição do elemento
print(frutas.index("jaca"))

#Len em tupla mostra a quantidade de elementos na tupla
print(len(frutas))
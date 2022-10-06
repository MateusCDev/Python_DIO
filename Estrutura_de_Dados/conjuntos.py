#Conjuntos são elementos que não contem itens duplicados mas sem ordem nos iteraveis
numeros =set([1,2,3,4,5,6,1])
print(numeros)

letras=set("abacaxi")
print(letras)


linguagens = {"python", "java", "python"}
print(linguagens)

numeros = list(numeros)
print(numeros)
print(numeros[0])

#Metodos classe set

#union
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_c = {6,7,8}

print(conjunto_a.union(conjunto_b))

#intersection recupera os elementos que são comuns em ambos conjuntos

print(conjunto_a.intersection(conjunto_b))

#difference recupera os elementos qde um conjunto que não esta contido no outro

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#symmetric_difference recupera os elementos que não estão contidos em ambos

print(conjunto_a.symmetric_difference(conjunto_b))

#issubset se um conjunto esta contido em outro é True se não é False

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#issuperset é o inverso do issubset

print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

#isdisjoint todos os elementos que não estão em um conjunto é True se estiver é False

print(conjunto_a.isdisjoint(conjunto_b)) # False
print(conjunto_b.isdisjoint(conjunto_c)) # True

#add passar um elemento em um conjunto caso ele não exista no conjunto

conjunto_c.add(9)
print(conjunto_c)

#clear limpar o conjunto
#copy copia o conjunto

#discard discarta um valor no conjunto

conjunto_c.discard(9)
print(conjunto_c)

#pop tira os valores a partir do inicio do conjunto

#remove ele tem a mesma função do discard so que ele irar apontar errro se passar um numero inexsistente no parametro

#len tamanho do conjunto
print(len(conjunto_a))

#verificar se um elemento esta no conjunto é com o in

print(2 in conjunto_a) #true


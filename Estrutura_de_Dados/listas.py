#Listas são mutaveis e podem colocar varios tipos de valor na lista 
frutas= []
print(frutas)
frutas = ["laranja","maca", "usa"]
print(frutas)
letras = list("python")
print(letras)
numeros = list(range(10))
print(numeros)
carro=["Ferrari", "F8", 4200000, 2020 , 2900, "São Paulo", True]
print(carro)

#Acessando um elemento na lista
print(frutas[0])
print(frutas[1])

#listas aninhadas  ou matriz bidimensional
matriz = [
    [1,"a",2],
    ["b",3,4],
    [6,5,"c"]
]

print(matriz[0])
print(matriz[0][0])

#Fatiamento de uma lista
print(letras[0:2])
print(letras[::-1])

#iterar listas
carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

#Saber o indice com enumerate dentro de um for
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")    

#Compreensão de listas
numeros = [1,2,3,4,5,6,7,8,9,10]
pares=[]

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
print(pares)

#Versão perfomatica
pares_v2 =[numero for numero in numeros if numero % 2 ==0]
print(pares)

# Modificando valores
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado) 


#Versão perfomatica
quadrado_v2=[numero**2 for numero in numeros]
print(quadrado_v2)


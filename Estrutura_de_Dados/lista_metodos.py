#Inserindo valores em uma lista com o metodo append
lista =[]

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print (lista)

#Metodo copy para copiar uma lista
l2 = lista.copy()
print(l2)

#Metodo clear para limpar lista
lista.clear()
print (lista)
print(l2)

#Metodo count para contar quantos objetos tem em uma lista
cores =["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("verde"))
print(cores.count("azul"))

#adicionando muitos elementos numa lista com metodo extends
linguagens =["JS", "C#", "Python"]

print(linguagens)

linguagens.extend(["Java", "R"])

print(linguagens)

#Revertendo a lista colocando ela ao contrario
linguagens.reverse()
print(linguagens)

#Ordenando lista com sort
linguagens.sort()
print(linguagens)
linguagens.sort(reverse = True)
print(linguagens)
linguagens.sort(key= lambda x: len(x))
print(linguagens)

#Verificando o tamanho da lista
print(len(linguagens))

#Metodo index para saber a posição do objeto em uma lista atravez da primeira ocorrência 
print(linguagens.index("R"))
print(linguagens.index("Java"))

#Excluindo elementos da lista com o pop que funciona por pilha ou seja o pop exclui o ultimo da lista por default

print(linguagens.pop())
print(linguagens.pop(0))
print(linguagens)

#Removendo o elemento da lista atraves do metodo remove passando o elemento em vez do indice

linguagens.remove("C#")
print(linguagens)
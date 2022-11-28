import itertools

string = input("String a ser permutada: ")

resultado = itertools.permutations(string, len(string)) # permuta uma sequencia de caracteres gerando ate 3 caracteres

#Gera a wordlist
for i in resultado:
    print(''.join(i))


# importando bibliotecas
import random
import string

tamanho = int(input("Digite o tamanho da senha que você deseja: ")) # tamanho da senha em inteiro
chars = string.ascii_letters + string.digits + '!@#$%&8()-=+' # recebe a estrutura da senha com letras maisuculas e minusculas, digitos numericos e caracteres especiais
rnd = random.SystemRandom() #gera numeros aleatorias a partir de fontes fornecidas do SO

while tamanho < 8:
    if tamanho > 8 : 
        print(''.join(rnd.choice(chars) for i in range(tamanho))) # o rnd ira escolher cada carecter do chars ate o range do tamanho da senha para juntar e printar a senhar gerada
    else:
        print("Tamanho de senha invalido!!")
        break 

nome= "Mateus"


print(nome.upper())#tudo em maiusculo
print(nome.lower())#tudo em minusculo
print(nome.title())# primeira letra em maiusculo

texto= " Ola mundo!  "

print(texto)
print(texto.strip())# corta  espaços em branco
print(texto.rstrip())# corta espaços a direita
print(texto.lstrip())# corta espaços a esquerda

menu = "Python"

print("####" + menu + "####")
print(menu.center(14, "#"))# mesma coisa que o de cima com o center
print("-".join(menu))#junta a cada iteração com o join


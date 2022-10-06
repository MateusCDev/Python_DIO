#Função é um bloco de condigo, programar em funções é o mesmo que programa de forma estruturada

#declarando funções e seus parametros
def exibir_mensagem():
    print("Olá mundo!")

def exibir_nome(nome ="Mateus"):
    print(f"Seja bem vindo {nome}")

#chamadas da função para executar
exibir_mensagem() 
exibir_nome() 
exibir_nome(nome="Cesar")     

#retorno de valores com return
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([5,10,15]))
print(retorna_antecessor_e_sucessor(20))   

#argumentos nomeados
def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro(**{"marca": "JEEP", "modelo": "Renegade", "ano": 2020, "placa": "RPG-1234"})#passando um dicionario com parametro **kwargs e *args vem como tupla

#Parâmetros especiais o que tiver antes da / é por posição obrigatorio e o que tiver depois da / é por nome = valor ou por posição opcional

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro("palio", 1999, "ABC-1234", marca ="Fiat", motor="1.0", combustivel="Gasolina") #valido

#Depois do * so por nome = valor
def criar_carro(*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo,ano,placa,marca,motor,combustivel)

criar_carro(modelo ="palio", ano=1999, placa="ABC-1234", marca ="Fiat", motor="1.0", combustivel="Gasolina") # valido   

#Objetos de primeira classe
def somar(a,b):
    return a + b

def subtrair(a,b):    
    return a - b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a} + {b} ou {a} - {b} é = {resultado}")    


exibir_resultado(5,15, subtrair)
exibir_resultado(5,15, somar)

op = somar

print(op(20,20))

#escopo global e local não é uma boa pratica usar variaveis globais por conta de manutenção

salario = 2000

def salario_bonus(bonus):
    global salario # o que esta fora do escopo tem que colocar o parametro global
    salario += bonus
    return salario

bonus = salario_bonus(500)    #2500
print(bonus)
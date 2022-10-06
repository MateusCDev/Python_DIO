#Dicionarios são um conjunto não ordenado de pares chave:valor, onde as chaves são unicas {}

pessoa = {"nome": "Mateus", "idade": 23}
print(pessoa)
pessoa= dict(nome="Mateus", idade=28)
print(pessoa)
pessoa["telefone"] = "9140-4976" #chave (telefone) valor (9140-4976)
print(pessoa)

#Acessando valores e substituindo valores
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

pessoa["nome"] = "Maria"
pessoa["idade"] = 15
pessoa["telefone"] = "9957-7242"

print(pessoa)

#dicionario com valores aninhados
contato = {
    "mateus.cesararaujo@gmail.com": {
        "nome": "Mateus",
        "telefone": "9140-4976"
    }
}
print(contato["mateus.cesararaujo@gmail.com"]["nome"]) #Mateus

#iterar dicionarios

for chave in contato:
    print(chave, contato[chave])

for chave, valor in contato.items(): # melhor forma com items
    print(chave,valor)

#Metodos da classe dict(dicionario)  

#copy copia o dicionario e adiciona em outro local da memoria
copia = contato.copy()
copia["mateus.cesararaujo@gmail.com"] = {"nome": "Duda"}
print(contato)
print(copia)

#fromkeys adciona chaves para o dicionario com valor vazio
Pessoas =dict.fromkeys(["nome", "telefone"])
print(Pessoas)

#get acessar a chave
print(contato.get("chave"))  
print(contato.get("chave", {}))#passando valor default se retornar vazio
print(contato.get("mateus.cesararaujo@gmail.com", {}))

#Keys retorna so a chave do dicionario
novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys())

#values retorna os valores do dicionario
print(novo_dicionario.values())

#pop remove os valores passando a chave como parametro

#popitem remove os valores de um dicionario sem passar chave como parametro

#update atualiza o dicionario se a chave não existir ele passa essa nova chave dentro de um dicionario que tem uma chave existente se atualizar uma chave existente ela sobrescreve o valor no dicionario

#setdeafult adciona um valor se o atributo não existir no dicionario se existir não substitui
Pessoas.setdefault("nome", "Gessica")
print(Pessoas)

Pessoas.setdefault("idade", 23)
print(Pessoas)

#in verifica se tem uma chave no dicionario
print("nome" in contato["mateus.cesararaujo@gmail.com"]) #true
print("mateus.cesararaujo@gmail.com" in contato) # True

#del tira objetos especificos  de um dicionario
del contato["mateus.cesararaujo@gmail.com"]["telefone"]
print(contato)

#clear limpa o dicionario
contato.clear()
print(contato)


nome ="Mateus"
idade = 23
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados ={"nome": "Mateus", "idade": 23}

#Old Style %s para string, %d para inteiro e %f para float
print("Ola, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#.format para interpolação com base em indices
print("Ola, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Ola, me chamo {3}. Eu tenho {0} anos de idade, trabalho como {2} e estou matriculado no curso de {1}.".format(idade, linguagem, profissao, nome))

print("Ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(idade=idade, linguagem=linguagem , profissao=profissao, nome=nome))

print("Nome : {nome}\nIdade :{idade}".format(**dados))

#f String
print(f"Nome: {nome}\nIdade: {idade}\nSaldo : {saldo:.2f}")

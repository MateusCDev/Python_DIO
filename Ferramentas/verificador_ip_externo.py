import re
import json
from urllib.request import urlopen

#pega a url do ipinfo em formato json
url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']


print(f""" --- DETALHES DO SEU IP EXTERNO ---
        IP: {ip}
        PAIS: {pais}
        CIDADE: {cidade}
        ORG: {org}
        REGIAO: {regiao} """)
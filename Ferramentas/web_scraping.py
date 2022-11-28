from bs4 import BeautifulSoup
import requests


# Recebe todo o conteudo da requisição http do site
site = requests.get("https://www.climatempo.com.br/").content 

# baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

# transformar o html em string e o print vai exibir o html
print(soup.prettify())
print(soup.title.string)
print(soup.find('Brasil'))
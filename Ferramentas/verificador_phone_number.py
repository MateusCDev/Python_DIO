import phonenumbers
from phonenumbers import geocoder

phone = input("Digite o telefone no formato +5571994104976: ")

# passa o numero digitado para tipo phonenumber
phone_numbers =  phonenumbers.parse(phone)

#Mostra a região do telefone
print(geocoder.description_for_number(phone_numbers, 'pt'))
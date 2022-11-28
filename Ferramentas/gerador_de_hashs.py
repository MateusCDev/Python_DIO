import hashlib

string = input("Digite o texto a ser gerado a hash: ")

menu = int(input(''' ### Menu - Escolha o tipo de HASH ### 
                    1) MD5
                    2) SHA1
                    3) SHA256
                    4) SHA512
                    Digite o numero do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8')) # Recebe um hash md5 em formato de bytes
    print(f"O hash MD5 da string é: {resultado.hexdigest()}")
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8')) # Recebe um hash sha1 em formato de bytes
    print(f"O hash SHA1 da string é: {resultado.hexdigest()}")    
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8')) # Recebe um hash sha256 em formato de bytes
    print(f"O hash SHA256 da string é: {resultado.hexdigest()}")
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8')) # Recebe um hash sha512 em formato de bytes
    print(f"O hash SHA512 da string é: {resultado.hexdigest()}")    
else:
    print("Opção invalida, digite o valor correto novamente!")    
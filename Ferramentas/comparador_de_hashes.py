import hashlib

arquivo1 = r"C:\Users\mateu\OneDrive\Documentos\Python DIO\Python_DIO\Ferramentas\a.txt"
arquivo2 = r"C:\Users\mateu\OneDrive\Documentos\Python DIO\Python_DIO\Ferramentas\b.txt"


hash1 = hashlib.new('ripemd160')
hash2 = hashlib.new('ripemd160')

# Abri o arquivo e ler ele no hash

hash1.update(open(arquivo1, 'rb').read()) 
hash2.update(open(arquivo2, 'rb').read())

# faz a comparação do hash
if hash1.digest() != hash2.digest():
    print(f'O arquivo:\n {arquivo1}\né diferente do arquivo:\n {arquivo2}')
    print('O hash do arquivo a.txt é : ', {hash1.hexdigest()})
    print('O hash do arquivo b.txt é : ', {hash2.hexdigest()})
else:
    print(f'O arquivo:\n {arquivo1}\né igual ao arquivo:\n {arquivo2}')   
    print('O hash do arquivo a.txt é : ', {hash1.hexdigest()})
    print('O hash do arquivo b.txt é : ', {hash2.hexdigest()}) 
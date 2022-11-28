import ctypes

atributo_ocultar = 0x02

retorno =  ctypes.windll.kernel32.SetFileAttributesW(r'C:\Users\mateu\OneDrive\Documentos\Python DIO\Python_DIO\Ferramentas\arquivo.txt', atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")



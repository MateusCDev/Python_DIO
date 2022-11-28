from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f'Piloto: {piloto} e  Carro: {trajeto}')



# recebe a função e os arqgumentos para sereme implementados como thread
t_carro1 = Thread(target=carro, args=[1, 'Mateus'])
t_carro2 = Thread(target=carro, args=[1.5, 'Gessica'])

# começa o processo dos dois carros
t_carro1.start()
t_carro2.start()
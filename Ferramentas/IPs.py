import ipaddress
import time
ip = '192.168.0.0/24'

# transforma a string ip em objeto ipaddres
rede = ipaddress.ip_network(ip, strict=False)

# imprime todos os ips da rede /24
for ip in rede:
    time.sleep(0.09)
    print(ip)
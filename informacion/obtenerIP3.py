#!/usr/bin/env Python
import socket
from binascii import hexlify
def formato_direccion_ip():
		
		equipo_remoto_a = socket.gethostbyname('www.twitter.com')
		equipo_remoto_b = socket.gethostbyname('www.unab.cl')
		#nombrepc1 = socket.gethostbyaddr(equipo_remoto_a)
		#nombrepc2 = socket.gethostbyaddr(equipo_remoto_b)
		
		for dir_ip in [equipo_remoto_a, equipo_remoto_b]:
					 empaquetada_ip = socket.inet_aton(dir_ip)
					 no_empaquetada_ip = socket.inet_ntoa(empaquetada_ip)
					 print ("Direccion Ip: %s => Empaquetada: %s, No Empaquetada: %s" %(dir_ip, hexlify(empaquetada_ip), no_empaquetada_ip))
					 #print("nombre de pc: " + nombrepc1)
					 #print("nombre de pc2: " + nombrepc2)

if __name__ == '__main__':
		formato_direccion_ip()
import socket
import sys

def banner(ip,puerto):
    s =socket.socket()
    s.connect((ip, puerto))
    print(str(s.recv(1024)))


def main():
    ip =input("ingresa la ip del objetivo: ")   
    port= int(input("Ingresa el puerto: "))
    banner(ip,port)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt():
        sys.exit()
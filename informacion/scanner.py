import sys
import socket

def main():
    target = input(" Ingrese la ip:")
    for port in range (1,81):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("El puerto {} se encuentr abierto".format(port))
        s.close()    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit
import requests
from os import path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help="Indica dominio victima")
parser = parser.parse_args()

def main():
    if parser.target:
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt', 'r')
            wordlist = wordlist.read().split('\n')

            for subdominios in wordlist:
                url = "http://"+subdominios+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("(+) Subdominio Descubierto: " + url)


    else:
        print("porfavor coloca subdominio valido")
        sys.exit

if __name__ == '__main(__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

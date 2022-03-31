import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Indica el dominio victima")
parser = parser.parse_args()


def main():
	if parser.target:
		if path.exists('subdominios.txt'):
			wordlist = open('subdominios.txt','r')
			wordlist = wordlist.read().split('\n')

			for subdominio in wordlist:
				url = "http://"+subdominio+"."+parser.target
				try:
					requests.get(url)
				except requests.ConnectionError:
					pass
				else:
					print("(+) Subdominio Descubierto: " + url)

			for subdominio in wordlist:
				url = "https://" + subdominio + "." + parser.target
				try:
					requests.get(url)
				except requests.ConnectionError:
					pass
				else:
					print("(+) Subdominio Descubierto: " + url)

	else:
		print("Porfavor coloca un subdominio valido")
		sys.exit()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
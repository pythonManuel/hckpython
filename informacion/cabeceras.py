import requests
import argparse
import sys

parse = argparse.ArgumentParser(description="detector de cabeceras")
parse.add_argument('-t','--target',help="objetivo")
parse = parse.parse_args()

def main():
    if parse.target:
        try:
            url = requests.get(url=parse.target)
            cabeceras = dict(url.headers)
            for cabecera in cabeceras:
                print(cabecera+" : "+cabeceras[cabecera])
        except:
            print("no se pudo establecer conexion")
    else:
        print("no hay objetivo definido")        
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit


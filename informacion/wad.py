import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help = "indica el sitio web")
parser = parser.parse_args()

def main():
    if parser.target:
        subprocess.run("wad -u" + parser.target + "> tecnologias.txt", shell=True)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit
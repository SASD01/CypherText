#Importamos las librerias para obtener datos aleatorios y manipular el entorno de la ejecución.
#Base de apoyo: “Cryptography-with-python-simple-substitution-cipher — Get Docs,” Getdoc.wiki, 2022. 
# https://getdoc.wiki/Cryptography-with-python-simple-substitution-cipher (accessed Feb. 25, 2022).
#  Inventwithpython.com, 2022. 
#https://inventwithpython.com/hacking/chapter17.html (accessed Feb. 25, 2022).
#E. Man, “Substitution Cipher Implementation with Python,” YouTube. Aug. 12, 2018, 
# Available: https://www.youtube.com/watch?app=desktop&v=lKFfmSbkeiw.
import sys
import base64
import hashlib
#Definimos el alfabeto
Alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Llave de Encriptado.
Cyphertext = b'KRUISTHEBESTTEAMINLATAM'
KEY = ''
#Definimos una funcion que le permita al usuario ingresar el mensaje para decifrarlo.
# Creamos una lista de todos los caracteres base64 w/ padding.
b64_chars = [c for c in 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/=']

def Funcionconvertir(string, type):
	# Tomando sha512 hash De la llave.
	hash = hashlib.sha512(KEY).hexdigest()
	# Copia de caracteres b64
	cipher = b64_chars[:]
	# Reorganizar el cifrado.
	for c in hash:
		char_int = int(c, 16)
		pos = 65 * (char_int / 15)
		# Mover el elemento al principio y revertir la lista de caracteres.
		cipher.insert(0, cipher.pop(int(pos)-1))
		cipher = cipher[::-1]
	sbox = {}
	for i, c in enumerate(b64_chars):
		sbox[c] = cipher[i]
	# Desencriptar
	if type == 'D':
		   sbox = dict((v, k) for k, v in sbox.items())
         for i, c in enumerate(string):
             string[i] = sbox[c]
             return ''.join(string)

def encrypt(string):
	string = [c for c in base64.b64encode(string.encode()).decode()]

	return Funcionconvertir(string, 'e')
def decrypt(string):
	string = [c for c in string.strip()]

	return base64.b64decode(Funcionconvertir(string, 'D')).decode()

if sys.argv[1] == '-E':
	print(encrypt(sys.stdin.read()))
if sys.argv[1] == '-D':
	try:
		print(decrypt(sys.stdin.read()))
	except:
		print('No se pudo desencriptar')
        
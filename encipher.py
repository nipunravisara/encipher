import base64
import os, shutil
import getopt, sys
from modules.logo import *
from modules.colors import colors
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]

home_dir = os.environ['HOME']
sourse_path = ''
password = ''
option = ''
key = ''

#capture user options, path and password
def getOptions():
	
	global option
	global password
	global sourse_path

	option = input(colors.BIBlue + "Encrypt or Decrypt [e/d] ?: " + colors.BIBlue)
	
	if option == 'e':
		sourse_path = input("Source Path [from home dir]: ")
		#password = input("Enter password: ")
		password = getpass("Enter password: ")
		print()
	elif option == "d":
		sourse_path = input("Encrypted file path [from home dir]: ")
		#password = input("Enter password: ")
		password = getpass("Enter password: ")
		print()


#generate key from user pw
def generateKey():

	global key
	global password

	userPassword = password.encode()
	salt = b'salt_'
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=100000,
		backend=default_backend()
		)
	key = base64.urlsafe_b64encode(kdf.derive(userPassword))
	print(colors.BIGreen + '🔐 Key generated.' + colors.BIGreen)


#encrypt files
def encryptFile():

	print("🔍 File search complete.")
	try:
		os.chdir(home_dir + sourse_path)
		print(os.getcwd())
	except:
		print(colors.BIWhite + "📂 No such directory! Try again" + colors.BIWhite)
		exit (0)

	os.mkdir('encrypted')
	fileNameList = os.listdir(home_dir + sourse_path)
	
	for file in fileNameList:
		if file.endswith(('.png', '.PNG', '.jpg', '.JPG', '.jpeg', 'JPEG', 'txt', 'pdf', 'mp3', 'mp4', 'mkv')):
			input_file = file
			output_file = file + '.enc'
			with open(input_file, 'rb') as f:
				data = f.read()

			fernet = Fernet(key)
			encrypted = fernet.encrypt(data)

			with open(output_file, 'wb') as f:
				f.write(encrypted)

			shutil.move(output_file, './encrypted')
			print(colors.BIWhite + "   ∟📜 Encrypting " + file + "..." + colors.BIWhite + colors.BIGreen + " Done!" + colors.BIGreen)

	#success message
	print(colors.BIGreen +  "✅ Encryption completed!" + colors.BIGreen)
	print()
	print(colors.BIBlue + "📦 All encrypted files are saved to " + colors.BIBlue + colors.BIWhite + os.getcwd() + "/encrypted" + colors.BIWhite)


#decrypt files
def decryptFile():

	print("🔍 File search complete.")
	try:
		os.chdir(home_dir + sourse_path)
	except:
		print("📂 No such directory! Try again")
		exit (0)

	os.mkdir('decrypted')
	fileNameList = os.listdir(home_dir + sourse_path)

	for file in fileNameList:
		if file.endswith(('.enc')):

			
			input_file = file
			decryptFileName = file.split('.')
			output_file = decryptFileName[0] + "." + decryptFileName[1]


			with open(input_file, 'rb') as f:
				data = f.read()

			fernet = Fernet(key)

			try:
				encrypted = fernet.decrypt(data)

				with open(output_file, 'wb') as f:
					f.write(encrypted)

				shutil.move(output_file, './decrypted')
				print(colors.BIWhite + "   ∟📜 Decrypting " + file + "..." + colors.BIWhite + colors.BIGreen + " Done!" + colors.BIGreen)
			except Exception as e: 
				print(colors.BIWhite + '🔒 Password does not match with encrypted password!' + colors.BIWhite)
				sys.exit(0)

	#success message
	print(colors.BIGreen + "✅ Decryption completed!" + colors.BIGreen)
	print()
	print(colors.BIBlue + "📦 All Decrypted files are saved to " + colors.BIBlue + colors.BIWhite + os.getcwd() + "/decrypted" + colors.BIWhite)



def main():

	global option
	global password
	global sourse_path

	#logo
	logo.start_banner()

	#if no arguments
	if argument_list == []:

		getOptions()
		if option == 'e':
			generateKey()
			encryptFile()
		elif option == 'd':
			generateKey()
			decryptFile()
		else: print( colors.BIWhite + '📛 Incorrect option, Try again!' + colors.BIWhite)

	#if any arguments is missing
	elif len(argument_list) > 0 and len(argument_list) <= 2:
		print("> Only " + str(len(argument_list)) + " arguments provided. Required 3 - (option, path, password)")
		print('🚧 Please enter all reqired arguments! or run "python encypher.py"') 
		exit()

	#if arguments
	else:
		option = argument_list[0]
		sourse_path = argument_list[1]
		password = argument_list[2]

		if option == '-e':
			generateKey()
			encryptFile()
		elif option == '-d':
			generateKey()
			decryptFile()
		else: print( colors.BIWhite + '📛 Incorrect option, Try again!' + colors.BIWhite)
		
	
	

#spark here
main()

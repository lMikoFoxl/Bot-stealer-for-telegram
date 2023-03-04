debug=1
log=1
test=1
versionserver ='0.0.5'
import socket
import keyboard
from socket import SHUT_RDWR
from key_generator.key_generator import generate
import random
from time import gmtime, strftime
import time
import os,sys
from pathlib import Path

port = 65124 
host =  '127.0.0.1'
def Key_Gen():
	key_genQuestion=int(input("I haven't keys, you want generate new keys?(1-yes,0-no): "))
	if key_genQuestion==1: 
		key_genQuestion=int(input("How much keys you need?: "))
	random.seed(strftime("%Y%H%M%S +0000", gmtime()))
	with open("keys",'w', encoding="utf-8") as f:
		i=0
		while i!=key_genQuestion:
			randomNumber=random.randint(1, 2419401299124)
			randomkey=generate(seed = randomNumber)
			randomkeyinstr=str(randomkey.get_key())
			f.write(randomkeyinstr+"\n")
			i=i+1
	f.close()
	if debug==1:print("Keys generated")
	if debug==1:print("Key_Gen: File closed")

my_file = Path("keys")
if my_file.is_file():
	if debug==1:print("I have keys and now don't need generate more keys")
else:
	Key_Gen()
	

def Search_key(keycheeck):
	try:
		with open("keys","r",encoding="utf-8")as file: 
			readfile= file.readlines()
			if debug == 1: print(readfile)
			for key in readfile:
				if debug == 1: print(key)
				if keycheeck+"\n" == key:
					if debug==1: print("Search_key: True")
					file.close()
					return 1
		file.close()
		if debug==1: print("Search_key: File closed")
	except Exception as errorSearch_Key:
		if debug== 1: print(errorSearch_Key)
		else: print("Search_Key: Error")
def Add_HardwareLock(idd,keycheeck):
	try:
		if debug==1: print("Add_HardwareLock: started")
		with open("keys","r+",encoding="utf-8")as file: 
			readfile= file.readlines()
			if debug == 1: print(readfile)
			for key in readfile:
				if debug == 1: print(key)
				if keycheeck+"\n" == key:
					if debug==1: print("Search_key: True")
					file.write(key+idd)
	except Exception as errorAdd_HardwareLock:
		if debug== 1: print(Add_HardwareLock)
		else: print("Add_HardwareLock: Error")
	print("Add_HardwareLock: File closed")
def Search_key_With_Hardware_Lock(keycheeck, idd):
	try:
		with open("keys","r",encoding="utf-8")as file: 
			readfile= file.readlines()
			if debug == 1: print(readfile)
			for key in readfile:
				if debug == 1: print(key)
				if keycheeck+"\n" == key:
					if debug==1: print("Search_key: True")
					file.close()
					return 1
	except Exception as errorSearch_key_With_Hardware_Lock:
		if debug== 1: print(Search_key_With_Hardware_Lock)
		else: print("Search_key_With_Hardware_Lock: Error")
	file.close()
	if debug==1: print("Search_key: File closed")
def openserv():
	global server
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((host, port))
	print("Server is work. \n   Port is:"+str(port)+"\n   Host is:"+ str(host))
	server.listen() 
def closeserver():
	print("SERVER CLOSED")
	server.close()
def exit():
    if keyboard.read_key() == "ctrl+c":
        print("You pressed p")
        sys.exit()
		

openserv()
while True:
	
	
	user, addr = server.accept()
	if log== 1: print(user)

	try:
		
		key = user.recv(1024) 
		versionfromuser = user.recv(1024)
		uuidfromuser = user.recv(1024)
		checkLicense = key.decode("utf-8")
		if debug == 1: print("Uuid: "+uuidfromuser.decode("utf-8"))
		if log == 1: print("I have key from user: "+checkLicense)
		checkversion = versionfromuser.decode("utf-8");
		if debug == 1: print("I have client's version: "+	checkversion) 
		if checkversion == versionserver:
			if Search_key(checkLicense) == 1:
				if log == 1:print("I checked key from user. It's true")
				user.sendall("kUe1k19AagsiojpfAbLemIalkylEgiCENChAtiELICtornaBIAlTolERYoUGhTEsceSlerTOnuKiLicePTiCitIvEticITermYoRSeApegYNwNYwC4KPxUf359Qpm0aCMr1T2Y5drXem4djWXQoufQNW994KFPLjMdTAhp5kVKZh57vfjcFEmiVGU0dBN4zYcvddvsf5188F8H9EPWH89TG4ph89rt8hopr9gt4esdgh8pra9tghfwap9t4894p8hgfvanpewsdfafsblksetlfgiuwsgbhftgbuefwilbgwfuibvbvbsbbdbfbfsbfbdueuru3417842781478156dfs78f8tgsf7sfd7sfd87s7fsf8sd78sfd78gs78f0E".encode("utf-8"))
			else:
				if Search_key_With_Hardware_Lock(checkLicense, uuidfromuser)==1:
					if log == 1:print("I checked key from user. It's true")
					user.sendall("kUe1k19AagsiojpfAbLemIalkylEgiCENChAtiELICtornaBIAlTolERYoUGhTEsceSlerTOnuKiLicePTiCitIvEticITermYoRSeApegYNwNYwC4KPxUf359Qpm0aCMr1T2Y5drXem4djWXQoufQNW994KFPLjMdTAhp5kVKZh57vfjcFEmiVGU0dBN4zYcvddvsf5188F8H9EPWH89TG4ph89rt8hopr9gt4esdgh8pra9tghfwap9t4894p8hgfvanpewsdfafsblksetlfgiuwsgbhftgbuefwilbgwfuibvbvbsbbdbfbfsbfbdueuru3417842781478156dfs78f8tgsf7sfd7sfd87s7fsf8sd78sfd78gs78f0E".encode("utf-8"))
				else:
					user.sendall("Error: invalid key".encode("utf-8"))
					if log == 1:print("Error: Invalid key")
			if not key:
				if log == 1:print("Fatal error: Haven't key from user")
		if checkversion!=versionserver:
			if log == 1:print("Fatal error: User client have old version ")
			user.sendall("Error: old version".encode("utf-8"))
	except Exception as error:

		if debug==1:
			print(error)
		print("Can't get data from user")
		closeserver()
		time.sleep(0.01)
		openserv()

		

	
user.close()

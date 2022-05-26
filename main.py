import requests
import socket
import sys
import time
import os

while True:
	try:
		def check_IPv4(address):
			try:
				if socket.inet_aton(str(address)):
					return True
			except:
				return False
		IPv4 = socket.gethostbyname (input ("Please enter the target's IPv4 adress: "))
		valid = check_IPv4(IPv4)
		if valid == False:
			print (f"IPv4 address {IPv4} is invalid!")
		else:
			try:
				url = 'http://ip-api.com/json/' + IPv4
				response = requests.get(url).json()
				if os.name == 'nt':
					os.system('cls')
				else:
					os.system('clear')
				print("-" * 50)
				print ("IPv4 Address: " + str (IPv4))
				print ("Country: " + response['country'])
				print ("Region: " +  response['regionName'])
				print ("City: " + response['city'])
				print ("Organization: " + response['org'])
				print ("Latitude: "+ str(response['lat']))
				print ("Longitude: "+ str(response['lon']))
				print("-" * 50)
			except KeyError:
				print (f"IPv4 address {IPv4} is private!")
	except KeyboardInterrupt:
		print ("\nExiting program")
		time.sleep(2.5)
		sys.exit()
	except socket.gaierror:
		print(f"\nIPv4 address is invalid!")

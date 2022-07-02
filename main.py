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
			print ("IPv4 address is invalid!")
		else:
			try:
				url = 'http://ip-api.com/json/' + IPv4
				response = requests.get(url=url, headers={'User-Agent' : 'Prowser/1.0 ()'}).json()
				if os.name == 'nt':
					os.system('cls')
				else:
					os.system('clear')
				print("-" * 75)
				print ("IPv4 Address: " + str(IPv4))
				print ("Country: " + str(response['country']))
				print ("Country Code: " + str(response['countryCode']))
				print ("Region: " +  str(response['regionName']))
				print ("Reigion Code: " + str(response['region']))
				print ("City: " + str(response['city']))
				print ("Zip Code: " + str(response['zip']))
				print ("Latitude: "+ str(response['lat']))
				print ("Longitude: "+ str(response['lon']))
				print ("Organization: " + str(response['org']))
				print ("Timezone: " + str(response['timezone']))
				print ("Internet Service Provider: " + str(response['isp']))
				print ("Autonomous System: " + str(response['as']))
				print("-" * 75)
			except KeyError:
				if os.name == 'nt':
					os.system('cls')
				else:
					os.system('clear')
				print ("IPv4 address is private!")
	except KeyboardInterrupt:
		print ("\nExiting program")
		time.sleep(2.5)
		sys.exit()
	except socket.gaierror:
		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
		print("IPv4 address is invalid!")

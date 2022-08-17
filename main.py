import requests
import socket
import sys
import time
import os
import platform

def main():
	while True:
		try:
			def check_IPv4(address):
				try:
					if socket.inet_aton(str(address)):
						return True
				except:
					return False
			IPv4 = socket.gethostbyname (input ("Please enter the target's IPv4 adress, DNS or hostname: "))
			valid = check_IPv4(IPv4)
			if valid == False:
				print ("IPv4 address is invalid!")
			else:
				try:
					url = 'http://ip-api.com/json/' + IPv4
					response = requests.get(url=url, headers={'User-Agent' : 'IP_WHOIS/1.0 (' + platform.system() + ' ' + os.name().touppercase() + ')'}).json()
					if os.name == 'nt':
						os.system('cls')
					else:
						os.system('clear')
					print ("-" * 75)
					print (f"IPv4 Address:  {str(IPv4)}")
					print (f"Country: " + str(response['country']))
					print (f"Country Code: " + str(response['countryCode']))
					print (f"Region: " +  str(response['regionName']))
					print (f"Reigion Code: " + str(response['region']))
					print (f"City: " + str(response['city']))
					print (f"Zip Code: " + str(response['zip']))
					print (f"Latitude: "+ str(response['lat']))
					print (f"Longitude: "+ str(response['lon']))
					print (f"Organization: " + str(response['org']))
					print (f"Timezone: " + str(response['timezone']))
					print (f"Internet Service Provider: " + str(response['isp']))
					print (f"Autonomous System: " + str(response['as']))
					print ("-" * 75)
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
if __name__ == '__main__':
    main()
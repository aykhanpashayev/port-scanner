#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
   target = socket.gethostbyname(sys.argv[1]) #Translates the hostname to IPv4
   
else:
   print("Invalid amount of arguments")
   print("Syntax: python3 scanner.py <ip>")

#Adding banner
print("-"*50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-"*50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
			s.close()

#If we like to exit the program

except KeyboardInterrupt:
	print("\nExiting the program.")
	sys.exit()

#If host name does not resolve
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
#If we are not even online or can not connect to the server
except socket.error:
	print("Could not connect to server.")
	sys.exit()

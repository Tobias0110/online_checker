#Tobias Ecker OE3TEC 2019

import os
import time

online = 1

while 1:
	sum = 0
	for x in range(3):
		response = os.system("ping -c 1 192.168.1.101") #returns 256 when ping failed
		sum = sum + response
		time.sleep(10)
		#print("summe: " + str(sum))

	if sum < 768:
		if online == 0:
			print("Wetterstation online")
			online = 1
			os.system("ssmtp example@gmail.com < mail_on.txt")
		else:
			print("Noch immer online")
	else:
		if online == 1:
			print("Wetterstation offline")
			online = 0
			os.system("ssmtp example@gmail.com < mail_off.txt")
		else:
			print("Noch immer offline")

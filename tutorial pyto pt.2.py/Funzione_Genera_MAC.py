import random
import string

def MAC_gen():
	mac_list = []
	digits = string.hexdigits
	for i in range(6):
		mac_list.append(random.choice(digits) + random.choice(digits))
	mac = ":".join(mac_list)
	return mac

print(MAC_gen())
		

	
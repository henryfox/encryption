from __future__ import division
import sys
from rand import rand
import math

alphabet = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "[", "]", "}", "|", ",", ":", ";", "'", '"', "<", ">", "?", " "]

passpharse = sys.argv[2][1:]
path = sys.argv[3][1:]

with open(path) as fi:
	fi = fi.read()

if sys.argv[1] == "-e":
	fl = len(fi)
	num = rand(fl)
	pl = len(passpharse)
	pass_phrase_full = []
	y = 0
	pass_phrase_list_nums = []
	oo = False
	
	passpharse_list = list(passpharse)
	
	for x in range(0, fl):
		if y >= pl:
			y = 0
		pass_phrase_full.append(passpharse_list[y])
		y += 1
	for x in pass_phrase_full:
		y = 0
		z = 0
		for y in alphabet:
			z += 1

			if y == x:
				break
		pass_phrase_list_nums.append(z)
	num_list = list(num)

	fi_list = list(fi)

	fi_list_nums = []
	fi_list_nums_final = []

	num_list_final = []

	for x in fi_list:
		y = 0
		z = 0
		for y in alphabet:
			z += 1

			if y == x:
				break
		fi_list_nums.append(z)

	for x in range(0, len(num_list)):
		num_list_final.append(str(int(num_list[x]) + int(pass_phrase_list_nums[x])))

	num_final = " ".join(num_list_final)
	
	for x in range(0, len(num_list)):
		fi_list_nums_final.append(str(int(num_list[x]) + int(fi_list_nums[x])))
	fi_nums_final = " ".join(fi_list_nums_final)

	try:
		save = sys.argv[4]
		if save == "-d":
			print num_final + " file " + fi_nums_final
		if save == "-s":
			try:
				save_location = argv[5]

				with open(save_location,"w") as fil:
					fil.write(num_final + " file " + fi_nums_final)
			except:
				"you did not enter a save location or the save location you enterd is not valid"
	except:
		with open(path,"w") as fil:
			fil.write(num_final + " file " + fi_nums_final)
from __future__ import division
import sys
from rand import rand
import math

alphabet = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "[", "]", "}", "|", ",", ":", ";", "'", '"', "<", ">", "?", " "]

passpharse = sys.argv[2][2:]
path = sys.argv[3]

with open(path[2:]) as fi:
	fi = fi.read()

if sys.argv[1] == "-e":
	fl = len(fi)
	num = rand(fl)
	pl = len(passpharse)
	nopl = str(fl / pl)
	nopll = nopl.split(".")
	pass_phrase_full = []
	y = 0
	pass_phrase_list_nums = []
	
	if len(nopll) == 2:
		nopl_frac = (float(nopl)).as_integer_ratio()
		if nopl_frac[1] < fl:
			nopl_frac_bn = math.floor(fl / nopl_frac[1])
			nopl_frac_tn = math.floor(nopl_frac[0] * nopl_frac_bn)
		else:
			nopl_frac_bn = math.floor(nopl_frac[1] / fl)
			nopl_frac_tn = math.floor(nopl_frac[0] / nopl_frac_bn)
	
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

	for x in fi_list:
		y = 0
		z = 0
		for y in alphabet:
			z += 1

			if y == x:
				break
		fi_list_nums.append(z)

	print fi_list_nums






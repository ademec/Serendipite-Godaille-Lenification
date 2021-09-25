import json
import random
import re

from constants import ALPHA, DATA_FOLDER, SURNAME_MODEL_FILENAME, LASTNAME_MODEL_FILENAME

def gen_word(model):
	word = ""
	i = 0
	j = 0
	k = -1
	while k != 0:
		r = random.uniform(0, 1)
		k = 0
		while model[i][j][k] < r:
			k += 1
		word += ALPHA[k]
		i = j
		j = k
	return word

def gen_surname():
	with open(DATA_FOLDER + SURNAME_MODEL_FILENAME, "r") as f:
		surname_model = json.load(f)
	surname = gen_word(surname_model)
	while len(surname) < 4:
		surname = gen_word(surname_model)
	
	# add capital letters
	surname = surname[0].upper() + surname[1:]
	starts = [match.start() for match in re.finditer("[-'\s]", surname)]
	for start in starts:
		surname = surname[:start+1] + surname[start+1].upper() + surname[start+2:]

	return surname

def gen_lastname():
	with open(DATA_FOLDER + LASTNAME_MODEL_FILENAME, "r") as f:
		lastname_model = json.load(f)
	lastname = gen_word(lastname_model)
	while len(lastname) < 4:
		lastname = gen_word(lastname_model)
	
	# add capital letters
	lastname = lastname[0].upper() + lastname[1:]
	starts = [match.start() for match in re.finditer("[-'\s]", lastname)]
	for start in starts:
		lastname = lastname[:start+1] + lastname[start+1].upper() + lastname[start+2:]

	return lastname
from os import listdir
from random import choice

def gen_abstract():
	abstract_dir = "data/fake_theses/"
	filename = choice(listdir(abstract_dir))
	with open(abstract_dir + filename, 'r', encoding="utf-8") as f:
		abstract_data = f.read()
	return abstract_data
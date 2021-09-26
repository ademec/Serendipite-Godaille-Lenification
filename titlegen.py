from os import listdir
from random import choice

def gen_title():
	title_dir = "data/fake_titles/"
	filename = choice(listdir(title_dir))
	with open(title_dir + filename, 'r', encoding="utf-8") as f:
		title_data = f.read()
	return title_data
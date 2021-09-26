from os import listdir
from random import choice
from base64 import b64encode

def gen_photo_b64():
	photo_dir = "data/fake_faces/"
	filename = choice(listdir(photo_dir))
	with open(photo_dir + filename, 'rb') as f:
		photo_data = f.read()
	return b64encode(photo_data).decode()

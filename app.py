from os import listdir
from random import choice

from flask import Flask, render_template, send_file

from wordgen.word import gen_surname, gen_lastname

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", name=gen_surname() + " " + gen_lastname().upper())

@app.route("/doc")
def doc():
	return render_template("doc.html")

@app.route("/name")
def name():
	return gen_surname() + " " + gen_lastname()

@app.route("/photo.jpg")
def photo():
	photo_dir = "data/fake_faces/"
	filename = choice(listdir(photo_dir))
	print(filename)
	return send_file(photo_dir + filename, mimetype="image/jpeg")

if __name__ == "__main__":
	app.run()

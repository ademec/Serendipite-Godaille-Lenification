from flask import Flask, render_template, send_file

from wordgen.word import gen_surname, gen_lastname
from photogen import gen_photo_b64

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html",
		name=gen_surname() + " " + gen_lastname().upper(),
		photo=gen_photo_b64()
	)

@app.route("/doc")
def doc():
	return render_template("doc.html")

@app.route("/name")
def name():
	return gen_surname() + " " + gen_lastname().upper()

@app.route("/photo")
def photo():
	return gen_photo_b64()

if __name__ == "__main__":
	app.run()

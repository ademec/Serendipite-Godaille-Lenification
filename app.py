from flask import Flask, render_template, url_for

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

@app.route("/photo")
def photo():
	return #url_for('static', )

if __name__ == "__main__":
	app.run()

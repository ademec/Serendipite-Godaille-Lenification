from flask import Flask, render_template

from wordgen.word import gen_surname, gen_lastname

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/name")
def surname():
	return gen_surname() + " " + gen_lastname()

if __name__ == "__main__":
	app.run()
from flask import Flask, render_template

from name_gen.name import gen_family_name, gen_surname

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/surname")
def surname():
	return 

if __name__ == "__main__":
	app.run()
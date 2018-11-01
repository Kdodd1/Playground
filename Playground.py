from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

@app.route('/play')
def index():

	return render_template("index.html")

@app.route('/play/<num>')
def num(num):
	return render_template("play.html", num = int(num))

@app.route('/play/<num>/<color>')
def numColor(num, color):
	return render_template("color.html", num = int(num), color= color)

if __name__ == "__main__":
	app.run(debug=True)
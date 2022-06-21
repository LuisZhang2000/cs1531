from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/home", methods=["GET", "POST"])
def home():
	return "This is my home page"
	
@app.route("/profile/<name>")
def profile(name):
	return render_template("names.html", names=name)
	
app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world"
	
@app.route("/home", methods=["GET", "POST"])
def home():
	return "This is my home page"
	
@app.route("/profile/<name>")
def profile(name):
	return "You are on " + name
	
app.run(debug=True)

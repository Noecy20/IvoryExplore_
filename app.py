from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def bienvenue():
    return render_template("bienvenu.html")

@app.route("/base")
def base():
    return render_template("base.html")

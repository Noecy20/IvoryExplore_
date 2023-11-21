from flask import Flask,render_template, url_for

app = Flask(__name__)

@app.route('/')
def bienvenue():
    return render_template("bienvenu.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants/restaurant.html")

@app.route("/hotel")
def hotel():
    return render_template("hotels/hotel.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)

 
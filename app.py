from flask import Flask,render_template, url_for

app = Flask(__name__)

@app.route('/')
def bienvenue():
    return render_template("bienvenu.html")


@app.route('/accueil/')
def accueil():
    return render_template("accueil.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants/restaurant.html")


@app.route("/hotel")
def hotel():
    return render_template("hotels/hotel.html")

@app.route("/nav/")
def nav():
    return render_template("./partial/navBar.html")
if __name__ == "__main__":
    app.run(debug=True)

 
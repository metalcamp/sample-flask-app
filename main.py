from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    text = "Yet another message from handler"
    current_year = datetime.datetime.now().year
    cities = ["Boston", "Vienna", "Paris"]
    return render_template("index.html", text=text, current_year=current_year, cities=cities)


@app.route("/about-me")
def about_me():
    return render_template("about-me.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run()

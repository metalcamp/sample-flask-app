from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    text = "Yet another message from handler"
    current_year = datetime.datetime.now().year
    cities = ["Boston", "Vienna", "Paris"]
    return render_template("index.html", text=text, current_year=current_year, cities=cities)


@app.route("/about-me", methods=["GET"])
def about_me():
    return render_template("about-me.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/contact", methods=["POST"])
def contact():
    # TODO validation

    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")


if __name__ == '__main__':
    app.run()

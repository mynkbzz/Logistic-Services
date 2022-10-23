from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def about():
    return render_template("about.html")


@app.route("/404.html")
def error():
    return render_template("404.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/feature.html")
def feature():
    return render_template("feature.html")


@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/price.html")
def price():
    return render_template("price.html")


@app.route("/quote.html")
def quote():
    return render_template("quote.html")


@app.route("/service.html")
def service():
    return render_template("service.html")


@app.route("/team.html")
def team():
    return render_template("team.html")


@app.route("/testimonial.html")
def testimonial():
    return render_template("testimonial.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)

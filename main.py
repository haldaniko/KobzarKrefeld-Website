from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/onecolumn")
def onecolumn():
    return render_template("onecolumn.html")


@app.route("/threecolumn")
def threecolumn():
    return render_template("threecolumn.html")


@app.route("/twocolumn1")
def twocolumn1():
    return render_template("twocolumn1.html")


@app.route("/twocolumn2")
def twocolumn2():
    return render_template("twocolumn2.html")


if __name__ == "__main__":
    app.run(debug=True)

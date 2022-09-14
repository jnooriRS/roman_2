from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/roman/")
def roman():
    return render_template("roman.html")


@app.route("/arabic/")
def arabic():
    return render_template("arabic.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

import requests as req
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=int(os.environ.get("PORT")),
            debug=True)


h = {'Authorization': 'YOUR_REST_KEY'}
resp = req.get("https://api2.isbndb.com/book/9781934759486", headers=h)
print(resp.json())

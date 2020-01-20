import os
from flask import Flask, render_template, url_for, request
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['DATABASE_URI'] = os.environ.get("MONGO_URI")


def search_result(search_text):
    """
    """
    resp = requests.get(
        url='http://www.omdbapi.com/?s=' + search_text + '&apikey=45a7f96')
    json = resp.json()
    results = json['Search']
    result_list = []
    for i in results:
        result_list.append(i)
    return(result_list) 

@app.route("/")
def index():
    """
    Renders the index.html template
    """
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Renders the register.html template
    """
    return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Renders the login.html template
    """
    return render_template("login.html")


@app.route("/profile")
def profile():
    """
    Renders the profile.html template
    """
    return render_template("profile.html")


@app.route("/results", methods=["POST"])
def results():
    """
    Renders the results.html template
    """
    if request.method == "POST":
        search_text = request.form['search']
        search_result(search_text)
        return render_template("results.html", movie_results=search_result(search_text))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)

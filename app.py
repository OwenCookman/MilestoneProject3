import os
import requests
from flask import Flask, render_template, url_for, request, flash, redirect, session
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['DATABASE_URI'] = os.environ.get("MONGO_URI")


def search_result(search_text):
    """
    """
    resp = requests.get(
        url='https://www.goodreads.com/search.xml?key=8U3Do6kokXXj0Ex1ipnQ&q="+ search_text +"')
    json = resp.json()
    library = json['result']
    result_list = []
    for i in library:
        result_list.append(i)


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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created successfully!", "success")
        return redirect(url_for("index"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Renders the login.html template
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "" and form.password.data == "":
            flash(f"Login Successful", "success")
            return redirect(url_for("profile"))
        else:
            flash(f"Login unsuccessful, please try again", "danger")
    return render_template("login.html", form=form)


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
        return render_template("results.html", book_result=search_result(search_text))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)

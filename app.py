import requests
import os
from flask import Flask, render_template, url_for, request, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '6a03625dd3632ca18bdaf40e76f478bb'


def search_result(search_text):
    resp = requests.get(url="http://openlibrary.org/search.json?q=" +
                        search_text + "&mode=ebooks&has_fulltext=true")
    json = resp.json()
    xx = json['docs']
    result_list = []
    for item in xx:
        if 'author_name' in item and 'first_publish_year' in item and 'publisher' in item and 'id_amazon' in item:
            result_list.append((item['title'], item['author_name'],
                                item['first_publish_year'], item['publisher'], item['id_amazon']))
            return result_list


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created successfully!", "success")
        return redirect(url_for("index"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
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
    return render_template("profile.html")


@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        search_text = request.form['search']
        search_result(search_text)
        return render_template("results.html",  book_result=search_result(search_text))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)

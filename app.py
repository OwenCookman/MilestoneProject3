import os
import requests
from flask_pymongo import PyMongo
from flask import Flask, render_template, url_for, request, redirect



APP = Flask(__name__)
APP.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
APP.config['MONGO_URI'] = os.environ.get("MONGO_URI")
API_KEY = os.environ.get("API_KEY")
DB = PyMongo(APP)


def search_result(search_text):
    """
    Function takes the variable search_text and sends the query to the API
    The result of the query returns in JSON format and is passed through a
    for loop which appends each item to the empty list result_list which is
    then returned.
    """
    resp = requests.get(
        url='http://www.omdbapi.com/?s=' + search_text + '&apikey=' + API_KEY)
    result = resp.json()
    search = result['Search']
    result_list = []
    for i in search:
        result_list.append(i)
    return result_list


@APP.route("/")
def index():
    """
    Renders the index.html template
    """
    return render_template("pages/index.html")



@APP.route("/results", methods=["POST"])
def results():
    """
    Renders the results.html template, the variable movie_results is passed
    to render the results from search_results()
    """
    if request.method == "POST":
        search_text = request.form['search']
        return render_template("pages/results.html", movie_results=search_result(search_text))


@APP.route("/movie/<imdb_id>")
def movie(imdb_id):
    """
The href of the generated <a> from results.html is taken from the URL
 and converted in to a python variable which is passed to the API
 the data from the API is then passed to the template movie.html
    """
    resp = requests.get(url='http://www.omdbapi.com/?i=' +
                        imdb_id + '&apikey=' + API_KEY)
    info = resp.json()
    return render_template("pages/movie.html", movie_info=info)


@APP.route("/add_review/<imdb_id>")
def add_review(imdb_id):
    """

    """
    resp = requests.get(url='http://www.omdbapi.com/?i=' +
                        imdb_id + '&apikey=' + API_KEY)
    info = resp.json()
    return render_template("pages/movie.html", movie_info=info)

if __name__ == "__main__":
    APP.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)

import os
import requests
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for


APP = Flask(__name__)
APP.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
APP.config['MONGO_URI'] = os.environ.get("MONGO_URI")
API_KEY = os.environ.get("API_KEY")
mongo = PyMongo(APP)
mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client.MoviestoreDB
col = db["Reviews"]


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
    search = result.get('Search', [])
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
 the data from the API is then passed to the template movie.html.
 A query is sent to the Mongo database to find any reviews with
 the movieID that corresponds with the imdb_id taken from the API
 this data is then iterated through and appended to an empty list
 which is passed back to the template to render.
    """
    resp = requests.get(url='http://www.omdbapi.com/?i=' +
                        imdb_id + '&apikey=' + API_KEY)
    info = resp.json()

    review_list = []

    get_reviews = mongo.db.Reviews.find({'movieID': imdb_id})
    for review in get_reviews:
        review_list.append(review)

    return render_template("pages/movie.html", movie_info=info, reviews=review_list)


@APP.route("/add_review/<imdb_id>")
def add_review(imdb_id):
    """
    Passes the same information from the movie() function but to the
     review.html template
    """
    resp = requests.get(url='http://www.omdbapi.com/?i=' +
                        imdb_id + '&apikey=' + API_KEY)
    info = resp.json()

    return render_template("pages/review.html", movie_info=info)


@APP.route("/submit_review/", methods=["POST"])
def submit_review():
    """
    The variable review is created by taking information from the form
     on the review.html template, this is then passed as an argument
      to the Mongo database. The page is then redirected to index.html
    """
    review = {'username': request.form.get('username'),
              'comments': request.form.get('comments'),
              'score': request.form.get('score'),
              'movieID': request.form.get('movieID')}
    mongo.db.Reviews.insert_one(review)
    return redirect(url_for('index'))

@APP.route("/edit_review/<review_id>", methods=["POST"])
def edit_review(review_id):
    """
    """
    old_review = mongo.db.Reviews.find_one({'_id': ObjectId(review_id)})

    info = old_review['movieID']
    username = request.form.get('username')
    comments = request.form.get('comments')
    score = request.form.get('score')

    review = {'username': username,
              'comments': comments,
              'score': score,
              'movieID': info}
    print(review)
    mongo.db.Reviews.replace_one(old_review, review)
    return render_template("pages/edit_review.html", movie_info=info)

@APP.route("/delete_review/<review_id>", methods=["POST"])
def delete_review(review_id):
    """
    The review_id generted in the form action for the delete review button
     is passed to the database which searches for the corresponding
     document and deletes it, then redirects to the index.
    """
    mongo.db.Reviews.delete_one({'_id': ObjectId(review_id)})

    return redirect(url_for('index'))



if __name__ == "__main__":
    APP.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)

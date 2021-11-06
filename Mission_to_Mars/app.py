
from logging import debug
from flask import Flask
from flask.templating import render_template
from flask_pymongo import PyMongo
from selenium import webdriver
from werkzeug.utils import redirect
import mars_scrape

app = Flask(__name__)
mongo = PyMongo(app, uri= "mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
   mars_dict = mongo.db.mars_dict.find_one()
   return render_template("index.html", mars= mars_dict)

@app.route("/scrape")
def scrape():
   mars_dict = mongo.db.mars_dict
   mars_data = mars_scrape.scrape()
   mars_dict.update({},mars_data, upsert=True)
   return "Success"

if __name__ == "__main__":
   app.run(debug=True)


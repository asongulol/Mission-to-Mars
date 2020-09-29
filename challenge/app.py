#use flask to render template
from flask import Flask, render_template
#use pyMongo to interact with Mongo DB
from flask_pymongo import PyMongo
#import scraping code
import scraping
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
#setup routes
@app.route("/")
def index():
   scrape()
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)
@app.route("/hemispheres")
def hemispheres():
   mars = mongo.db.mars.find_one()
   return render_template("hemispheres.html", mars=mars['hemispheres'])
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"  
#.update(query_parameter, data, options)
if __name__ == "__main__":
   app.run()
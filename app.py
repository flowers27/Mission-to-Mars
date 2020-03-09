from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


@app.route("/")
def index():
    mars_db_dict = mongo.db.mars.find_one()
    return render_template("index.html", mars_html=mars_db_dict)


@app.route("/scrape")
def scraper():
    mars_db_dict = mongo.db.mars 
    mars_scrape_data = scrape_mars.scrape()
    mars.update({}, mars_scrape_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

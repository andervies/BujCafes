from flask import Flask, render_template, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'


# Creating the database model
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cafe_name = db.Column(db.String, unique=True, nullable=False)
    location = db.Column(db.String, nullable=False)
    open = db.Column(db.DateTime)
    close = db.Column(db.DateTime)
    coffee_rating = db.Column(db.Numeric, nullable=False)
    wifi_rating = db.Column(db.Numeric, nullable=False)
    power_rating = db.Column(db.Numeric, nullable=False)


@app.route("/")
def home():
    return "Hi, Dev. Welcome to Buj Cafes"


if __name__ == "__main__":
    app.run(debug=True)

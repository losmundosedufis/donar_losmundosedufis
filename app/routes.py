from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gracias")
def gracias():
    return render_template("gracias.html")
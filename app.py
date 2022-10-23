from re import A
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guardian")
def guardian():
    return render_template("guardian.html")
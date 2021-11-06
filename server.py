from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import fields, validators
import requests, time #requests module, a more general purpose: interacting with APIs


app= Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/courses")
def courses():
    return render_template("pay.html")

@app.route("/termsOfUse")
def termsOfUse():
    return render_template("termsOfUse.html")

if __name__== "__main__":
    app.run()
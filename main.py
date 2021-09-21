#!/usr/bin/python
# -*- coding: Utf-8 -*-

from datetime import datetime
from flask import Flask, render_template, request, redirect, session
import os
import logic


app = Flask(__name__,
    template_folder=os.path.abspath('html/'))

app.secret_key = "ahcestcontulaspas"
app.debug = True

@app.route('/login')
def login():
    return render_template("login.html")


# @app.route("/checklogin",  methods=['POST', 'GET'])
# def checklogin():
#     if true:
#         return redirect("/")
#     else:
#         return redirect("/login")


@app.route("/checkreg",  methods=['POST', 'GET'])
def checkreg():
    pass
    psd = request.form["inscpseudo"]
    mail = request.form["inscuser"]
    mdp = request.form["inscmdp"]
    c_mdp = request.form["conf_inscmdp"]
    # capcha = request.form["capcha"]
    if logic.register(mail, mdp, psd) == 255:
        pass


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    # website_url = '51.178.41.82:5050'
    # app.config['SERVER_NAME'] = website_url
    app.run()

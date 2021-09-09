#!/usr/bin/python
# -*- coding: Utf-8 -*-

from datetime import datetime
from flask import Flask, render_template, request, redirect, session
import os


app = Flask(__name__,
    template_folder=os.path.abspath('html/'))

app.secret_key = "ahcestcontulaspas"
app.debug = True

@app.route('/index.html')
def home2():

    return redirect("/")
@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    website_url = '51.178.41.82:5050'
    app.config['SERVER_NAME'] = website_url
    app.run()

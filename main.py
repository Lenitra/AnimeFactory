#!/usr/bin/python
# -*- coding: Utf-8 -*-

from datetime import datetime
from flask import Flask, render_template, request, redirect, session
import os


app = Flask(__name__, 
    template_folder=os.path.abspath('html/'),
    static_folder=os.path.abspath('static/'))

app.secret_key = "ahcestcontulaspas"
app.debug = True


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=50000)


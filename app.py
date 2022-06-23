from flask import Flask, render_template, redirect
from icyparser import IcyParser
import os
import random

application = Flask(__name__)

ip = IcyParser()
url = 'http://ice1.somafm.com/groovesalad-128-mp3'
ip.getIcyInformation(url)


@application.route("/")
def index():
    songname = ip.icy_streamtitle.replace("';StreamUrl='http://somafm.com/logos/512/groovesalad512.png", "")
    return render_template("index.html", songname=songname)

if __name__ == "__main__":
    application.run(host="localhost", port=1337, debug=True)
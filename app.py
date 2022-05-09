from turtle import down
from flask import Flask, render_template, json, redirect, url_for
from flask import request
from random import choice
import os
import time
import urllib.request
# code citation download and save from url https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know
import requests
import random
# code citation select random line from file https://www.w3resource.com/python-exercises/file/python-io-exercise-15.php

app = Flask(__name__)


def downloadImgs():
    cwd = os.getcwd()
    cwd = cwd + "\static\img"
    list = open("bg_image_urls.txt").read().splitlines()
        # with open("bg_image_urls.txt").read().splitlines()
    for line in list:
        img = line
        urllib.request.urlretrieve(img, os.path.join(cwd, os.path.basename(img)))
    return

##### Routes #####

# home page that has links to other pages
@app.route('/')
def index():
    if request.method == 'GET':
        if request.values.get('randomWallpapers') == "randomWallpapers":
            f = open("image_request.txt", "w")
            f.write("fetch_images")
            f.close()
            downloadImgs()
            # cwd = os.getcwd()
            # cwd = cwd + "\static\img"
            # img = random.choice(os.listdir(cwd))
            # # urllib.request.urlretrieve(img, os.path.join(cwd, os.path.basename(img)))
            return redirect(url_for("randomWallpaper"))
        if request.values.get('getWallpapers') == 'getWallpapers':
            return redirect(url_for("wallpapers"))
    return render_template("index.html")


@app.route('/wallpapers')

# code citation, how to return img directory and url https://stackoverflow.com/questions/26052561/how-to-list-all-image-files-in-flask-static-subdirectory
def wallpapers():
    downloadImgs()
    imageName = os.listdir(os.path.join(app.static_folder, 'img'))  # microservices will download to static/img
    return render_template('wallpapers.html', imageName = imageName)

@app.route('/randomWallpaper')

# code citation, how to return img directory and url https://stackoverflow.com/questions/26052561/how-to-list-all-image-files-in-flask-static-subdirectory
def randomWallpaper():
    imageName = choice(os.listdir(os.path.join(app.static_folder, 'img')))  # microservices will download to static/img
    return render_template('randomWallpaper.html', imageName = imageName)


##### Listener #####
if __name__ == "__main__":
    # Start the app on port 3000, it will be different once hosted
    app.run(port=31277, debug=True)

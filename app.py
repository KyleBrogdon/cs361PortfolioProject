from flask import Flask, render_template, json, redirect, url_for
from flask import request
from random import choice
import os

app = Flask(__name__)


##### Routes #####

# home page that has links to other pages
@app.route('/')
def index():
    if request.method == 'GET':
        if request.values.get('randomWallpapers') == "randomWallpapers":
            pass  # call to microservice scrapper here
            return redirect(url_for("randomWallpaper"))
        if request.values.get('getWallpapers') == 'getWallpapers':
            return redirect(url_for("wallpapers"))
    return render_template("index.html")


@app.route('/wallpapers')

# code citation, how to return img directory and url https://stackoverflow.com/questions/26052561/how-to-list-all-image-files-in-flask-static-subdirectory
def wallpapers():
    imageName = os.listdir(os.path.join(app.static_folder, 'img'))  # microservices will download to static/img
    print(imageName)
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

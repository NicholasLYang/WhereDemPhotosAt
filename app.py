from flask import Flask, render_template, request, session, redirect, url_for
import user
import urllib2, json
import utils

gKey ="AIzaSyDbrIKnZ-fJcUxd636duQL8khuiekjC5pQ"
fKey = '20dd8b0f53a96c73c31c2f9ec7a22c9f'

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")

@app.route('/map', methods=["GET","POST"])
def mapPage():
    print "hello"
    if request.method == "POST":
        form = request.form
        number = form["Number"]
        tag = form["Tag"]
        addr = form['Address']
        radius = form['Radius']
        latlng = utils.getLatLng(addr)
        searchphotos = utils.searchPhotos(number, tag, latlng, radius)
        photos = utils.findLocation(searchphotos)
        photos = utils.checkfordupe(photos)
        if len(searchphotos) == 0:
            center = utils.getLatLng(form['Address'])
            return render_template("map.html", address=center, API_KEY=gKey)
        if len(searchphotos) < int(number):
            error = "Only " + len(searchphotos) + " photos were found"
            return render_template("map.html", photos=photos, error=error, API_KEY=gKey)
        else:
            return render_template("map.html", photos=photos, API_KEY=gKey)
    else:
        return url_for(home())


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gP_3.hV[KE-P@|{pE5+Iv+m}"
    app.run('0.0.0.0', port=8000)

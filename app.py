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
        photos = utils.findLocation(utils.searchPhotos(form["Number"], form["Tag"], utils.getLatLng(form['Address']), form["Radius"] ) )
        return render_template("map.html", photos=photos, API_KEY=gKey)
    else:
        photos =[
        {"latitude":40.6,"longitude":-73.9},
        {"latitude":41,"longitude":-74}
        ]
        return render_template("map.html", photos=photos, API_KEY=gKey)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gP_3.hV[KE-P@|{pE5+Iv+m}"
    app.run('0.0.0.0', port=8000)

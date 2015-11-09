from flask import Flask, render_template, request, session, redirect, url_for
import user
import urllib2, json

gKey="AIzaSyDbrIKnZ-fJcUxd636duQL8khuiekjC5pQ"
fKey = '20dd8b0f53a96c73c31c2f9ec7a22c9f'

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    if request.method == "POST":
        tag = request.form['Tag']
        session['Longitude'] = request['Longitude']
        session['Latitude'] = request['Latitude']
        session['Number'] = request['Number']
        return url_for(getFlickrInfo())
    else:
        return render_template("home.html")

@app.route('/map')
def mapPage():
    coords =[
    {"latitude":40.6,"longitude":-73.9},
    {"latitude":41,"longitude":-74}
    ]

    return render_template("map.html", coords=coords, API_KEY=gKey)





@app.route('/test')
def getFlickrInfo():

    return render_template("location.html", longitude = longitude, latitude=latitude)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gP_3.hV[KE-P@|{pE5+Iv+m}"
    app.run('0.0.0.0', port=8000)

from flask import Flask, render_template, request, session, redirect, url_for
import user, utils
import urllib2, json


gKey ="AIzaSyDbrIKnZ-fJcUxd636duQL8khuiekjC5pQ"


fKey = '20dd8b0f53a96c73c31c2f9ec7a22c9f'

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    if request.method == "POST":
        session['Tag'] = request.form['Tag']
        session['Longitude'] = request.form['Longitude']
        session['Latitude'] = request.form['Latitude']
        session['Number'] = request.form['Number']
        return url_for(mapPage())
    else:
        return render_template("home.html")

@app.route('/map')
def mapPage():
    photos = utils.searchPhotos(session['Number'], session['Tag'], session['Latitude'], session['Longitude'])
    coords = utils.findLocation(photos)
    
    ''' coords =[
    {"latitude":40.6,"longitude":-73.9},
    {"latitude":41,"longitude":-74}
    ]
    '''
    return render_template("map.html", coords=coords, gKey = gKey )





    
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gP_3.hV[KE-P@|{pE5+Iv+m}"
    app.run('0.0.0.0', port=8000)

from flask import Flask, render_template, request, session, redirect, url_for
import user
import urllib2, json



app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/test')
def getFlickrInfo():
    import urllib2, json
    method = 'flickr.photos.geo.getLocation'
    photoid = '21870769994'
    key = '20dd8b0f53a96c73c31c2f9ec7a22c9f'
    uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&method=%s&api_key=%s&photo_id=%s'
    url = uri%(method, key, photoid)
    request = urllib2.urlopen(url)
    result = request.read()
    translated = json.loads(result)
    longitude = translated['photo']['location']['longitude']
    latitude =  translated['photo']['location']['latitude']        
    return render_template("location.html", longitude = longitude, latitude=latitude)
    
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gP_3.hV[KE-P@|{pE5+Iv+m}"
    app.run('0.0.0.0', port=8000)

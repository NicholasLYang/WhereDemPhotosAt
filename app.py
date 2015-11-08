from flask import Flask, render_template, request, session, redirect, url_for
import user

API_KEY="AIzaSyDbrIKnZ-fJcUxd636duQL8khuiekjC5pQ"

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("Home.html")

@app.route('/map')
def mapPage():
    coords =[
    {"latitude":100,"longitude":100},
    {"latitude":200,"longitude":100},
    {"latitude":300,"longitude":100},
    {"latitude":400,"longitude":100},
    {"latitude":500,"longitude":100},
    {"latitude":-100,"longitude":100},
    {"latitude":-200,"longitude":100},
    ]

    return render_template("map.html", coords=coords, API_KEY=API_KEY )


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "gP_3.hV[KE-P@|{pE5+Iv+m}"
    app.run('0.0.0.0', port=8000)

from flask import Flask, render_template
import requests
import json
import os
#hello my guy
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/roms")
def roms():
    return render_template("roms.html")

@app.route("/Emulators")
def Emulators():
    return render_template("Emulators.html")

@app.route("/News")
def News():
 url = ('https://newsapi.org/v2/everything?'
       'q=emulation OR retro gaming OR console emulator&'
       'sortBy=publishedAt&'
       'language=en&'
       'apiKey=a8085ac3b4ff4f22a5d05f167a5e1188')

 response = requests.get(url)
 data = response.json()
 articles = data["articles"]

 return render_template("News.html", data=articles)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

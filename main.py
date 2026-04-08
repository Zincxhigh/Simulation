from flask import Flask, render_template, request
import requests
import json
import os

app = Flask(__name__)

API_KEY = "cbece997cf864fafbd850ffa930b6e43"
USERNAME = "admin"
PASSWORD = "55664455"

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
 articles = data ["articles"]

 return render_template("News.html", data=articles)

@app.route("/Modding")
def Modding():
   return render_template("Modding.html")

@app.route("/Games", methods=["GET","POST"])
def Games():
    Games = []
    query = ""

    if request.method == "POST":
        query = request.form.get("search")

    page = request.args.get("page", 1)
    url = f"https://api.rawg.io/api/games?key={API_KEY}&platforms=1,7,18,17,19,83,23&page={page}&page_size=20&search={query}"
    response = requests.get(url)
    data = response.json()
    Games = data.get('results', [])

    return render_template("Games.html", Games=Games, page=int(page), query=query)

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            return render_template("welldone.html")
        else:
         return render_template("admin.html", error="Invalid username or password")
    return render_template("admin.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
    
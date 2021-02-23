from flask import Flask


app = Flask(__name__)
app.static_folder = "./"


@app.route("/<file>/", methods=["GET", "POST"])
def appfilex(file):
    return app.send_static_file(file)


@app.route('/')
def munk():
    return app.send_static_file('index.html')

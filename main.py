from flask import Flask
from flask import Response
from flask import render_template


app = Flask("My app")


@app.route('/')
def index():
    return render_template("index.html", message="Саня пашел в жёппу!")
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
   return render_template("heatmap.html")


@app.route('/accident')
def analytics():
   return render_template("accidentviz.html")

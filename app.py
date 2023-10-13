from flask import Flask
import json


app = Flask(__name__)

@app.route("/")
def index():
   
    return "<h1>OLá Mundo</h1>"



app.run(debug=True)
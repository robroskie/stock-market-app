from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/main/")
def main(name=None):
    return render_template('main.html', name=name)
    
@app.route("/base/")
def base(name=None):
    return render_template('base.html', name=name)
    

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



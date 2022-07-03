from flask import Flask
from flask import request
from flask import render_template

import finance as fi

app = Flask(__name__)

@app.route("/main/")
def main(name=None):
    return render_template('base.html', name=name)
    
@app.route("/base/")
def base(name=None):
    return render_template('base.html', name=name)
    

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/calculate_result')
def calculate_result():
    start = str(request.args.get('dateStart'))
    end = str(request.args.get('dateEnd'))
    print(str(start) + '    is a')
    fi.generatePlot(start, end)
    return 'hi'
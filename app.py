from flask import Flask
from flask import request
from flask import render_template
import json
import time

import matplotlib 
matplotlib.use('Agg')

import yfinance as yf
import matplotlib.pyplot as plt


import numpy as np

import matplotlib.cbook as cbook
import mplfinance as mpf

import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)



@app.route("/main/")
def main(name=None):
    return render_template('base.html', name=name)
    
@app.route("/base/")
def base(name=None):
    return render_template('base.html', name=name)
    
@app.route("/tests/")
def test(name=None):
    # msft = yf.Ticker("MSFT")
    # hist = msft.history(start='2020-01-01', end='2022-12-01')
    # mpf.plot(hist, savefig = 'static/plot7.png')
    return "<p>Hello, World!</p>"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/calculate_result', methods=['GET'])
def calculate_result():
    msft = yf.Ticker("MSFT")
    hist = msft.history(start='2020-01-01', end='2022-12-01')
    mpf.plot(hist, savefig = 'static/plot7.png')

    # time.sleep(10)
    start = str(request.args.get('dateStart'))
    end = str(request.args.get('dateEnd'))

    # hist = msft.history(start=start, end=end)

    # msft = yf.Ticker("MSFT")
    # hist = msft.history(start='2020-01-01', end='2022-12-01')
    # mpf.plot(hist, savefig = 'static/plot7.png')

    path='images/temp/plot.png'  
    return json.dumps({path:path}), 200, {'Content-Type':'application/json'} 


@app.route('/calculate_result', methods=['GET'])
def generatePlot(startDate, endDate):
    msft = yf.Ticker("MSFT")
    hist = msft.history(start='2020-01-01', end='2022-12-01')
    mpf.plot(hist, savefig = 'static/plot9.png')



if __name__ == '__main__':
    app.run(debug=True)
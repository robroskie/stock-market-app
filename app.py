from flask import Flask
from flask import request
from flask import render_template
import json
import time
import os

import matplotlib 
matplotlib.use('Agg')

import yfinance as yf
import matplotlib.pyplot as plt


import numpy as np

import matplotlib.cbook as cbook
import mplfinance as mpf

import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_url_path="/static", static_folder="static")



@app.route("/main/")
def main(name=None):
    return render_template('base.html', name=name)

    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/calculate_result', methods=['GET'])
def calculate_result():
    start = str(request.args.get('dateStart'))
    end = str(request.args.get('dateEnd'))

    msft = yf.Ticker("MSFT")
    hist = msft.history(start=start, end=end)
    if os.path.exists('static/images/plot9.png'):
        os.remove('static/images/plot9.png')
    mpf.plot(hist, savefig = 'static/images/plot9.png')

    # time.sleep(3)


    # hist = msft.history(start=start, end=end)

    # msft = yf.Ticker("MSFT")
    # hist = msft.history(start='2020-01-01', end='2022-12-01')
    # mpf.plot(hist, savefig = 'static/plot7.png')

    # path='images/temp/plot.png'  
    # return json.dumps({path:path}), 200, {'Content-Type':'application/json'} 

    return 'hi'


# @app.route('/calculate_result', methods=['GET'])
# def generatePlot(startDate, endDate):
#     msft = yf.Ticker("MSFT")
#     hist = msft.history(start='2020-01-01', end='2022-12-01')
#     mpf.plot(hist, savefig = 'static/images/plot9.png')



if __name__ == '__main__':
    app.run(debug=True)
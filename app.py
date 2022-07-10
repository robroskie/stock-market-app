from flask import Flask
from flask import request
from flask import render_template
import os

import matplotlib 
matplotlib.use('Agg')

import mplfinance as mpf
import yfinance as yf

import getTicker as gt

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

    # or should this be done as client-side validation?
    # flash('date range...')

    msft = yf.Ticker("MSFT")
    hist = msft.history(start=start, end=end)
    if os.path.exists('static/images/plot9.png'):
        os.remove('static/images/plot9.png')
    mpf.plot(hist, savefig = 'static/images/plot9.png')

    return 'updated'


@app.route('/get_ticker', methods=['GET'])
def get_ticker():
    searchVal = str(request.args.get('searchVal'))
    tickers = gt.getTicker(searchVal)

    # or should this be done as client-side validation?
    # flash('date range...')

    return tickers

if __name__ == '__main__':
    app.run(debug=True)
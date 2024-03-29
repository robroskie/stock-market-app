from flask import Flask
from flask import request
from flask import render_template
import os

import matplotlib 
matplotlib.use('Agg')

import mplfinance as mpf
import yfinance as yf

import getTicker as gt
import getNews as gn


app = Flask(__name__, static_url_path="/static", static_folder="static")

@app.route("/main/")
def main(name=None):
    return render_template('main.html', name=name)

    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/calculate_result', methods=['GET'])
def calculate_result():
    start = str(request.args.get('dateStart'))
    end = str(request.args.get('dateEnd'))
    tck = ''
    vals = ''

    if 'ticker' in request.args:
        tck = str(request.args.get('ticker'))

    # flash('date range...')
    if tck != '':
        vals = yf.Ticker(tck)
    else:    
        vals = yf.Ticker("MSFT")
    hist = vals.history(start=start, end=end)
    if os.path.exists('static/images/plot9.png'):
        os.remove('static/images/plot9.png')
    mpf.plot(hist, savefig = 'static/images/plot9.png')

    return 'updated'

@app.route('/get_ticker', methods=['GET'])
def get_ticker():
    searchVal = str(request.args.get('searchVal'))
    tickers = gt.getTicker(searchVal)

    return tickers

@app.route('/get_news', methods=['GET'])
def get_news():
    ticker = str(request.args.get('ticker'))
    tickerSYMBOL = ticker.split("Symbol: ")

    # news = gn.getNews(ticker)
    print('ticker: (flask)' + tickerSYMBOL)
    news = gn.getNews('tickerSYMBOL')

    return news


if __name__ == '__main__':
    app.run(debug=True)
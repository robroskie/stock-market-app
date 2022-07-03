import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import mplfinance as mpf

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# startDate = '2020-01-01'
# endDate = '2022-12-01'

# get historical market data
# hist = msft.history(start=startDate, end=endDate)



# print(hist)





# plt = mpf.plot(hist, savefig = 'templates/images/temp/plot.png')


def generatePlot(startDate, endDate):
    hist = msft.history(start=startDate, end=endDate)
    plt = mpf.plot(hist, savefig = 'templates/images/temp/plot.png')
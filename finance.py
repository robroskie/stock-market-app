
import yfinance as yf
import mplfinance as mpf
# get stock info
# msft.info

# startDate = '2020-01-01'
# endDate = '2022-12-01'

# get historical market data
# hist = msft.history(start=startDate, end=endDate)



# print(hist)





# plt = mpf.plot(hist, savefig = 'templates/images/temp/plot.png')


# def generatePlot(startDate, endDate):
msft = yf.Ticker("MSFT")
hist = msft.history(start='2020-01-01', end='2022-12-01')
mpf.plot(hist, savefig = 'static/plot7.png')
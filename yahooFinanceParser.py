from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

ticker = yf.Ticker("WBA")
# print(ticker)
# print(ticker.get_recommendations())
# recommendation = ticker.get_recommendations()
# print(type(recommendation))
#
# print(recommendationThisMonth[0]*recommendationThisMonth[1])


# print(ticker.get_analyst_price_targets())
# print(ticker.info['volume'])
# print(ticker.info['averageVolume10days'])
# print(ticker.info['averageVolume'])
# print(ticker.info)
# print(type(ticker.info))
# for thing in ticker.info.keys():
#     print(thing, ticker.info[thing])
def getInfoOfTicker(ticker):
    ticker = yf.Ticker(ticker)
    info = None
    try:
        # ticker = yf.Ticker(ticker)
        info = ticker.info['volume']
        # print(info)
        info = True
        recommendationThisMonth = ticker.get_recommendations().iloc[0].tolist()[1:]
        return [recommendationThisMonth, ticker.get_analyst_price_targets(), ticker.info['currentPrice']]
    except:
        # return "NO INFO"
        print("NO INFO")
        pass
    print("here")
    if not info:
        return "NO INFO"
    else:
        return [ticker.get_recommendations(), ticker.get_analyst_price_targets()]

# print(getInfoOfTicker("WBA"))
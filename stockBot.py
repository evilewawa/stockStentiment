import redditApiParser
import geminiParser
import yahooFinanceParser


def getInfo():
    posts = redditApiParser.getPosts()
    # for post in posts - not using this because i want to limit length of running time + dunno how requests work
    for i in range(len(posts)):
        post = posts[i]
        # print(post)
        ticker = geminiParser.askGemini("what is the stock ticker in this text: '" + post[0] + post[1] +
                                        "'. Respond only with the ticker. If no ticker, respond with 'NO TICKER'")
        ticker = ticker.strip('\n')
        print(ticker)
        # print(ticker, type(ticker))
        # print(ticker == "NO TICKER")
        if ticker != "NO TICKER":
            # print("ticker: " + ticker)
            tickerInfo = yahooFinanceParser.getInfoOfTicker(ticker)
            if tickerInfo != "NO INFO":
                # print(tickerInfo)
                recommendation, recommendationGood = tickerInfo[0], False
                priceTarget, priceTargetGood = tickerInfo[1], False
                currPrice, currPriceGood = tickerInfo[2], False
                total = 0
                for i in range(len(recommendation)):
                    total += recommendation[i] * (2-i)
                recommendationGood = total >= 10
                currPriceGood = currPrice <= 1
                priceTargetGood = (priceTarget['median'] + priceTarget['mean'])/2 > currPrice * 3
                if recommendationGood and currPriceGood and priceTargetGood:
                    print(ticker + " sounds like a good idea")
                else:
                    print(ticker + " sounds like a bad idea")

getInfo()
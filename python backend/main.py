import investments
import news
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import random
import json
# Investment Simulator

# Pass time
def passTime(months):
    global time
    global portfolio
    for i in range(months):
        time += 1

        # Update news
        for event in newsEvents:
            event.update()
            # Remove old news
            if event.over:
                newsEvents.remove(event)
        # Generate news
        newsEvents.append(news.generateNewsEvent(random.sample(investmentSources, random.randint(1, 3))))

        # Update investment stats
        for investment in market:
            investment.update(newsEvents)
        # Update portfolio
        portfolio.update()

# Create test investments
investmentSources = []
apple = investments.InvestmentSource("Apple", "Company")
usGovt = investments.InvestmentSource("US Government", "Government")
bofa = investments.InvestmentSource("Bank of America", "Bank")
investmentSources.append(apple)
investmentSources.append(usGovt)
investmentSources.append(bofa)
market = []
market.append(investments.Stocks(apple, 100, 0.2, "AAPL"))
market.append(investments.Bonds(usGovt, 100, 0.1, "USG", 3, True, 0.052))
market.append(investments.CDs(bofa, 100, 0.05, "BAC", 3, True, 0.052))

# Create news event list
newsEvents = []


# Create player portfolio
global portfolio
portfolio = investments.Portfolio(10000)

# Time
global time
time = 0


# API
app = Flask(__name__)
@app.route("/test/")
def test():
    value = {
        "test": "test"
    }
    value.headers.add('Access-Control-Allow-Origin', '*')
    return json.dumps(value)

@app.route("/market/")
@cross_origin()
def getMarket():
    value = [
        {"name": str(market[i]), "price": (market[i].price)} for i in range(len(market))
    ]
    return json.dumps(value)

@app.route("/portfolio/")
@cross_origin()
def getPortfolio():
    global portfolio
    value = {
        "funds": portfolio.funds,
        "worth": portfolio.total_worth(),
        "shares": [{str(portfolio.shares[share]): portfolio.shares[share].shares} for share in portfolio.shares]
    }
    return json.dumps(value)

@app.route("/time/")
@cross_origin()
def getTime():
    global time
    return{"time": time}

@app.route("/investment/<string:investment>/")
@cross_origin()
def getInvestment(investment):
    global market
    for i in range(len(market)):
        if str(market[i].id) == investment:
            return jsonify((str(market[i]), str(market[i].price)))
    return jsonify("Investment not found")

@app.route("/buy/<int:index>/<int:shares>/")
@cross_origin()
def buy(index, shares):
    global portfolio
    global market
    portfolio.buy(market[index], shares)
    return json.dumps({"success": True})

@app.route("/sell/<int:index>/<int:shares>/")
@cross_origin()
def sell(index, shares):
    global portfolio
    global market
    portfolio.sell(list(portfolio.shares)[index], shares)
    return json.dumps({"success": True})

@app.route("/wait/<int:months>/")
@cross_origin()
def wait(months):
    global time
    passTime(months)
    return json.dumps({"success": True})

@app.route("/news/")
@cross_origin()
def getNews():
    value = [
        {"title": str(newsEvents[i].title), "description": str(newsEvents[i].description)} for i in range(len(newsEvents))
    ]
    return json.dumps(value)

if __name__ == "__main__":
    app.run(port=1080)



def main():

    while(True):
        # Prompt user for action: buy, sell, or quit
        action = input("Buy, sell, wait, or quit? ")
        if action == "quit":
            break
        elif action == "buy":
            # List investments in order with index
            for i in range(len(market)):
                print(i, market[i])
            # Prompt user for investment index
            index = int(input("Which investment? "))
            # Prompt user for number of shares
            shares = int(input("How many shares? "))
            # Buy shares
            portfolio.buy(market[index], shares)
        elif action == "sell":
            # List owned shares in order with index
            for i in range(len(portfolio.shares)):
                print(i, list(portfolio.shares)[i])
            # Prompt user for owned share index
            index = int(input("Which owned share? "))
            # Prompt user for number of shares
            shares = int(input("How many shares? "))
            # Sell shares
            portfolio.sell(list(portfolio.shares)[index], shares)
        elif action == "wait":
            # Increment time
            wait = int(input("How many months? "))
            passTime(wait)
        else:
            print("Invalid action")
            continue
        # Print portfolio worth
        print("Portfolio worth:", portfolio.total_worth())
        # Print owned shares
        print("Owned shares:")
        for share in portfolio.shares:
            print(portfolio.shares[share].investment, portfolio.shares[share].shares)
        # Print funds
        print("Funds:", portfolio.funds)

# Run main
if __name__ == "__main__":
    #main()
    pass
import investments
from flask import Flask
from flask import jsonify
# Investment Simulator

# Pass time
def passTime(months):
    global time
    global portfolio
    for i in range(months):
        time += 1
        # Update investment stats
        for investment in market:
            investment.update()
        # Update portfolio
        portfolio.update()

# Create test investments
apple = investments.InvestmentSource("Apple", "Company")
usGovt = investments.InvestmentSource("US Government", "Government")
bofa = investments.InvestmentSource("Bank of America", "Bank")
market = []
market.append(investments.Stocks(apple, 100, 0.2, "AAPL"))
market.append(investments.Bonds(usGovt, 100, 0.1, "USG", 3, True, 0.052))
market.append(investments.CDs(bofa, 100, 0.05, "BAC", 3, True, 0.052))


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
    return "Test"

@app.route("/market/")
def getMarket():
    return jsonify([(str(investment), str(investment.price)) for investment in market])

@app.route("/portfolio/")
def getPortfolio():
    global portfolio
    return jsonify((str(portfolio.funds), str(portfolio.total_worth()), [(str(portfolio.shares[share]), str(portfolio.shares[share].shares)) for share in portfolio.shares]))

@app.route("/time/")
def getTime():
    global time
    return jsonify(time)

@app.route("/investment/<string:investment>/")
def getInvestment(investment):
    global market
    for i in range(len(market)):
        if str(market[i].id) == investment:
            return jsonify((str(market[i]), str(market[i].price)))
    return jsonify("Investment not found")

@app.route("/buy/<int:index>/<int:shares>/")
def buy(index, shares):
    global portfolio
    global market
    portfolio.buy(market[index], shares)
    return jsonify("Success")

@app.route("/sell/<int:index>/<int:shares>/")
def sell(index, shares):
    global portfolio
    global market
    portfolio.sell(list(portfolio.shares)[index], shares)
    return jsonify("Success")

@app.route("/wait/<int:months>/")
def wait(months):
    global time
    passTime(months)
    return jsonify("Success")

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
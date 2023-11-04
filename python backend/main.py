import investments
# Investment Simulator

# Create test investments
apple = investments.InvestmentSource("Apple", "Company")
usGovt = investments.InvestmentSource("US Government", "Government")
bofa = investments.InvestmentSource("Bank of America", "Bank")
market = []
market.append(investments.Stocks(apple, 100, 0.2, "AAPL"))
market.append(investments.Bonds(usGovt, 100, 0.1, "USG", 3, True, 0.052))
market.append(investments.CDs(bofa, 100, 0.05, "BAC", 3, True, 0.052))

# Create player portfolio
portfolio = investments.Portfolio(10000)

while(True):
    # Prompt user for action: buy, sell, or quit
    action = input("Buy, sell, or quit? ")
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
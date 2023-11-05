import random


class InvestmentSource:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Investment:
    def __init__(self, source, price, risk, id):
        self.source = source
        self.price = price
        self.risk = risk
        self.id = id
    
    def __eq__(self, other):
        return self.id == other.id
    
    def __hash__(self):
        return hash(self.id)
    
    def update(self, newsEvents):
        # Randomly change price based on risk
        self.price *= (1 + random.uniform(-self.risk, self.risk))
        # Update price based on news events and risk
        for event in newsEvents:
            if self.source in event.sources:
                self.price *= (1 + event.effect * (1 + self.risk))
        # Ensure price is at least 1
        if self.price < 1:
            self.price = 1

class Stocks(Investment):
    def __init__(self, source, price, risk, id):
        super().__init__(source, price, risk, id)

    def __str__(self):
        return f"{self.source.name} stock ({self.id})"

class Bonds(Investment):
    def __init__(self, source, price, risk, id, duration, insurance, interest):
        super().__init__(source, price, risk, id)
        self.duration = duration
        self.insurance = insurance
        self.interest = interest

    def __str__(self):
        return f"{self.source.name} bond ({self.id})"
        

class CDs(Investment):
    def __init__(self, source, price, risk, id, duration, insurance, interest):
        super().__init__(source, price, risk, id)
        self.duration = duration
        self.insurance = insurance
        self.interest = interest

    def __str__(self):
        return f"{self.source.name} CD ({self.id})"

class Gold(Investment):
    def __init__(self, source, price, risk, id):
        super().__init__(source, price, risk, id)

    def __str__(self):
        return f"{self.source.name} gold ({self.id})"

class Crypto(Investment):
    def __init__(self, source, price, risk, id):
        super().__init__(source, price, risk, id)

    def __str__(self):
        return f"{self.source.name} cryptocurrency ({self.id})"

class MutualFunds(Investment):
    def __init__(self, source, price, risk, id):
        super().__init__(source, price, risk, id)

    def __str__(self):
        return f"{self.source.name} mutual fund ({self.id})"


class OwnedShare:
    # A record of shares of an investment owned by a player.  It is not an investment itself.
    def __init__(self, investment, shares):
        self.investment = investment
        self.shares = shares
    
    def worth(self):
        return self.investment.price * self.shares
    
    def __eq__(self, other):
        return self.investment == other.investment

    def __hash__(self):
        return hash(self.investment)
    
    def update(self):
        pass

class OwnedStock(OwnedShare):
    # A record of shares of a stock owned by a player.  It is not an investment itself.
    def __init__(self, investment, shares):
        super().__init__(investment, shares)

    def __str__(self):
        return f"{self.investment.source.name} stock ({self.investment.id})"

class OwnedBond(OwnedShare):
    # A record of shares of a bond owned by a player.  It is not an investment itself.
    # It has an age, which is the number of months since it was bought.
    def __init__(self, investment, shares):
        super().__init__(investment, shares)
        self.age = 0
        self.matured = False
        self.value = investment.price * shares

    def __str__(self):
        return f"{self.investment.source.name} bond ({self.investment.id})"

    def update(self):
        self.age += 1
        self.value *= (1 + self.investment.interest)
        if self.age >= self.investment.duration:
            self.matured = True
    
    def worth(self):
        return self.value

class OwnedCD(OwnedShare):
    # A record of shares of a CD owned by a player.  It is not an investment itself.
    # It has an age, which is the number of months since it was bought.
    def __init__(self, investment, shares):
        super().__init__(investment, shares)
        self.age = 0
        self.value = investment.price * shares
        self.matured = False

    def __str__(self):
        return f"{self.investment.source.name} CD ({self.investment.id})"

    def update(self):
        self.age += 1
        self.value = self.investment.price * (1 + self.investment.interest)
        if self.age >= self.investment.duration:
            self.matured = True
    
    def worth(self):
        return self.value

class OwnedGold(OwnedShare):
    # A record of shares of gold owned by a player.  It is not an investment itself.
    def __init__(self, investment, shares):
        super().__init__(investment, shares)

    def __str__(self):
        return f"{self.investment.source.name} gold ({self.investment.id})"

class OwnedCrypto(OwnedShare):
    # A record of shares of a cryptocurrency owned by a player.  It is not an investment itself.
    def __init__(self, investment, shares):
        super().__init__(investment, shares)

    def __str__(self):
        return f"{self.investment.source.name} cryptocurrency ({self.investment.id})"

class OwnedMutualFund(OwnedShare):
    # A record of shares of a mutual fund owned by a player.  It is not an investment itself.
    def __init__(self, investment, shares):
        super().__init__(investment, shares)

    def __str__(self):
        return f"{self.investment.source.name} mutual fund ({self.investment.id})"
    

class Portfolio:
    def __init__(self, initial_funds):
        self.shares = {}
        self.funds = initial_funds

    def total_worth(self):
        return sum(self.shares[s].worth() for s in self.shares)
    
    def buy(self, investment, shares):
        if self.funds < investment.price * shares:
            raise ValueError("You do not have enough funds")
        self.funds -= investment.price * shares
        if investment in self.shares:
            self.shares[investment].shares += shares
        else:
            self.shares[investment] = OwnedStock(investment, shares) if isinstance(investment, Stocks) else \
                OwnedBond(investment, shares) if isinstance(investment, Bonds) else \
                OwnedCD(investment, shares) if isinstance(investment, CDs) else \
                OwnedGold(investment, shares) if isinstance(investment, Gold) else \
                OwnedCrypto(investment, shares) if isinstance(investment, Crypto) else \
                OwnedMutualFund(investment, shares) if isinstance(investment, MutualFunds) else \
                None

    def sell(self, ownedshare, shares):
        if ownedshare not in self.shares:
            raise ValueError("You do not own this investment")
        if self.shares[ownedshare].shares < shares:
            raise ValueError("You do not own enough shares")
        self.shares[ownedshare].shares -= shares
        if self.shares[ownedshare].shares == 0:
            del self.shares[ownedshare]
        self.funds += ownedshare.price * shares

    def update(self):
        # Update owned shares
        for share in self.shares:
            self.shares[share].update()
        # Remove any owned bonds/cds that have matured and add their worth to funds
        for share in list(self.shares):
            if isinstance(self.shares[share], (OwnedBond, OwnedCD)) and self.shares[share].matured:
                self.funds += self.shares[share].worth()
                del self.shares[share]
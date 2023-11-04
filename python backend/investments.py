


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

class Stocks(Investment):
    def __init__(self, source, price, risk, id):
        super().__init__(source, price, risk, id)

class Bonds(Investment):
    def __init__(self, source, price, risk, id, duration, insurance, interest):
        super().__init__(source, price, risk, id)
        self.duration = duration
        self.insurance = insurance
        self.interest = interest
        self.age = 0

class CDs(Investment):
    def __init__(self, source, price, risk, id, duration, insurance, interest):
        super().__init__(source, price, risk, id)
        self.duration = duration
        self.insurance = insurance
        self.interest = interest
        self.age = 0

class Gold(Investment):
    def __init__(self, source, price, risk, id):
        super().__init__(source, price, risk, id)

class Crypto(Investment):
    def __init__(self, source, price, risk, id):
        super().__init__(source, price, risk, id)

class MutualFunds(Investment):
    def __init__(self, source, price, risk, id):
        super().__init__(source, price, risk, id)


class OwnedShare:
    def __init__(self, investment, shares):
        self.investment = investment
        self.shares = shares
    
    def worth(self):
        return self.investment.price * self.shares
    
    def __eq__(self, other):
        return self.investment == other.investment

    def __hash__(self):
        return hash(self.investment)
    

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
            self.shares[investment] = OwnedShare(investment, shares)

    def sell(self, ownedshare, shares):
        if ownedshare not in self.shares:
            raise ValueError("You do not own this investment")
        if self.shares[ownedshare].shares < shares:
            raise ValueError("You do not own enough shares")
        self.shares[ownedshare].shares -= shares
        self.funds += ownedshare.price * shares

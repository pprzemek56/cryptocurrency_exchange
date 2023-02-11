class Transaction:
    def __init__(self, token, price, amount, value, fee, extra_fee):
        self.token = token
        self.price = price
        self.amount = amount
        self.cost = value + fee + extra_fee

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

class Transaction:
    def __init__(self, token, amount, value, fee, extra_fee):
        self.token = token
        self.amount = amount
        self.cost = value + fee + extra_fee
        self.return_price = None

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token


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

    @property
    def return_price(self):
        return self._return_price

    @return_price.setter
    def return_price(self, return_price):
        self._return_price = return_price

    def count_return_price(self):
        self._return_price = self.cost / self.amount

class Account:
    def __init__(self, account_id, description="None", balance=0.0):
        self.account_id = account_id
        self.description = description
        self.balance = balance
        self.transactions = []

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        self._transactions = transactions

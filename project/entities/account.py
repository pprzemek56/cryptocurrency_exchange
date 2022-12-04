class Account:
    def __init__(self, account_id, transaction_id, description="None", balance=0.0):
        self.account_id = account_id
        self.transaction_id = transaction_id
        self.description = description
        self.balance = balance

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
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self._transaction_id = transaction_id
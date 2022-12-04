from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, trading_pair_name="XXX/XXX", price=0.0,
                 value=0.0, type_of_transaction="default", stop_loss=0.0,
                 take_profit=0.0, liquidation_price=0.0, status="default",
                 is_profitable=False, crate_date_time=datetime.now(), liquidation_date_time=datetime.now()):
        self.transaction_id = transaction_id
        self.trading_pair_name = trading_pair_name
        self.price = price
        self.value = value
        self.type_of_transaction = type_of_transaction
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.liquidation_price = liquidation_price
        self.status = status
        self.is_profitable = is_profitable
        self.crate_date_time = crate_date_time
        self.liquidation_date_time = liquidation_date_time

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self._transaction_id = transaction_id

    @property
    def trading_pair_name(self):
        return self._trading_pair_name

    @trading_pair_name.setter
    def trading_pair_name(self, trading_pair_name):
        self._trading_pair_name = trading_pair_name

    @property
    def price(self):
        return self._price


    @price.setter
    def price(self, price):
        self._price = price

    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, value):
        self._value = value

    @property
    def type_of_transaction(self):
        return self._type_of_transaction


    @type_of_transaction.setter
    def type_of_transaction(self, type_of_transaction):
        self._type_of_transaction = type_of_transaction

    @property
    def stop_loss(self):
        return self._stop_loss


    @stop_loss.setter
    def stop_loss(self, stop_loss):
        self._stop_loss = stop_loss

    @property
    def take_profit(self):
        return self._take_profit

    @take_profit.setter
    def take_profit(self, take_profit):
        self._take_profit = take_profit

    @property
    def liquidation_price(self):
        return self._liquidation_price

    @liquidation_price.setter
    def liquidation_price(self, liquidation_price):
        self._liquidation_price = liquidation_price

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def is_profitable(self):
        return self._is_profitable

    @is_profitable.setter
    def is_profitable(self, is_profitable):
        self._is_profitable = is_profitable

    @property
    def crate_date_time(self):
        return self._crate_date_time

    @crate_date_time.setter
    def crate_date_time(self, crate_date_time):
        self._crate_date_time = crate_date_time

    @property
    def liquidation_date_time(self):
        return self._liquidation_date_time

    @liquidation_date_time.setter
    def liquidation_date_time(self, liquidation_date_time):
        self._liquidation_date_time = liquidation_date_time

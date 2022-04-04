from datetime import datetime


class Account:
    def __init__(self, start_money):
        self._balance = 0
        if start_money != 0:
            self._balance = start_money
        self._log = []
        self._log.append([self.get_datetime(), start_money, self._balance])

    def get_balance(self):
        return self._balance

    def deposit(self, deposit_money):
        if deposit_money >= 0:
            self._balance += deposit_money
        else:
            raise Exception("Invalid money amount.")
        self._log.append([self.get_datetime(), deposit_money, self._balance])
        return self._balance

    def withdraw(self, withdraw_money):
        if withdraw_money >= 0:
            self._balance -= withdraw_money
        else:
            raise Exception("Invalid money amount.")
        self._log.append([self.get_datetime(), -withdraw_money, self._balance])
        return self._balance

    def get_datetime(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_log(self):
        log_string = f'{"Time":<22s}{"Amount":<10s}Balance'
        for datetime, amount, balance in self._log:
            log_string += f"\n{datetime:<22s}{amount:<+10d}{balance}"
        return log_string

    def clear_log(self):
        self._log = []

import unittest
from unittest.mock import patch
from account import Account
from datetime import datetime


class AccountTest(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Account(10).get_balance(), 10)

    def test_deposit_withdraw(self):
        self.assertEqual(Account(10).deposit(1), 11)
        self.assertEqual(Account(10).withdraw(1), 9)

    @patch("account.Account.get_datetime", return_value="31/03/2022 16:54:02")
    def test_log(self, get_datetime):
        account = Account(500)
        account.deposit(100)
        account.deposit(240)
        account.withdraw(240)
        log_string = (
            "Time                  Amount    Balance\n"
            "31/03/2022 16:54:02   +500      500\n"
            "31/03/2022 16:54:02   +100      600\n"
            "31/03/2022 16:54:02   +240      840\n"
            "31/03/2022 16:54:02   -240      600"
        )
        self.assertEqual(account.get_log(), log_string)


if __name__ == "__main__":
    unittest.main()

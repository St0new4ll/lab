import pytest
from account import *


class Test:
    def setup_method(self):
        self.acct1 = Account("John")
        self.acct2 = Account("Jane")

    def test_init(self):
        assert self.acct1.get_name() == 'John'
        assert self.acct1.get_balance() == 0
        assert self.acct2.get_name() == 'Jane'
        assert self.acct2.get_balance() == 0

    def test_deposit(self):
        assert self.acct1.deposit(100.15) is True
        assert self.acct1.get_balance() == pytest.approx(100.15, abs=0.001)
        assert self.acct2.deposit(0) is False
        assert self.acct2.deposit(-10) is False
        assert self.acct2.deposit(300) is True
        assert self.acct2.get_balance() == 300

    def test_withdraw(self):
        self.acct1.deposit(330.15)
        assert self.acct1.withdraw(50) is True
        assert self.acct1.withdraw(50.14) is True
        assert self.acct1.get_balance() == pytest.approx(230.01, abs=0.001)
        self.acct2.deposit(20)
        assert self.acct2.withdraw(0) is False
        assert self.acct2.withdraw(60) is False

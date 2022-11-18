
class Account:
    def __init__(self, name):
        """
        param name: Sets the name for the account
        Initializes the account balance at $0
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float):
        """
        Function to deposit a specified value into the account

        param amount: Value to be deposited into the account, expected to be a float greater than 0
        :return: True if deposited successfully, False if unsuccessful
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float):
        """
        Function to withdraw a specified value from the account
        :param amount: Value to be withdrawn from the account, expected to be a float greater than 0, but less than the
        account balance
        :return: True if withdrawn successfully, False if unsuccessful
        """
        if amount > self.__account_balance:
            return False
        elif amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        """
        Prints the account balance
        :return: Prints balance
        """
        print(self.__account_balance)

    def get_name(self):
        """
        Prints the name of the account
        :return: Prints name
        """
        print(self.__account_name)

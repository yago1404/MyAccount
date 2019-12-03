from Accounts.User import User


class Account(User):
    def __init__(self, user_name, password, account_number, agency_number):
        super(Account, self).__init__(user_name, password)
        self.__agency_number = agency_number
        self.__account_number = account_number
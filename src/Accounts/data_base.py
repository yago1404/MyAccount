from Accounts.Account import Account

users = {}
day = 1
user = Account(None, None, None, None)


def setUser(new_user):
    global user
    user = new_user

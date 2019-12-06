from until_functions.exceptions import getInput
from until_functions.grafic_interface import mensage
from until_functions.data_base import users
from Accounts.Account import Account
from random import randrange


def creatAccount():
    new_user_name = getInput("Entre com o nome de usuário\n=>", str)
    if new_user_name in users or new_user_name == "":
        print("Essse nome de usuário ja existe, ou não é aceito")
        return
    new_user_password = getInput("Entre com a nova senha\n=>", str)
    if new_user_password == "":
        print("É preciso colocar algum valor para a senha")
        return

    new_user_account_number = randrange(100, 10000)
    new_user_agency = getInput("Entre com o numero da agencia bancária", int, range(0, 100000))
    new_user = Account(new_user_name, new_user_password, new_user_account_number, new_user_agency)

    users[new_user_name] = new_user
    mensage("Usuário {} criado com sucesso. O número da sua conta é {}".format(new_user_name, new_user_account_number))

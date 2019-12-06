from abc import ABC
from until_functions.data_base import users
from random import randrange
from Accounts.Account import Account
from until_functions.exceptions import getInput
from Menu.Menu import Menu


class MainMenu(Menu, ABC):

    def __init__(self):
        self.__methods = [None, self.creatAccount, self.login]
        self.__methods_name = ["Void", "Criar conta", "Fazer login"]
        self.exec()

    def showMenu(self):
        for i in range(1, len(self.__methods)):
            print("({}) {}".format(i, self.__methods_name[i]))

    def exec(self):
        while True:
            self.showMenu()
            option = getInput("Entre com a opção desejada\n=>", int, range(1, 3))

            if option == -1:
                return
            elif option != -100:
                self.__methods[option]()

    @staticmethod
    def creatAccount():
        while True:
            user_name = getInput("Entre com o nome de usuário que deseja\n=>", str)
            if user_name == "" or user_name in users:
                print("Usuário invalido ou ja existente")
                continue
            break
        while True:
            password = getInput("Entre com a senha que deseja\n=>", str)
            if password == "":
                print("Entre com uma senha válida")
                continue
            break
        account_number = randrange(1000, 9999)
        agency_number = 10
        print(user_name, password, agency_number, account_number)
        new_user = Account(user_name, password, account_number, agency_number)
        users[user_name] = new_user
        print("Novo usuário criado com sucesso")

    def login(self):
        pass

from abc import ABC
from until_functions.data_base import users, getDay
from random import randrange
from Accounts.Account import Account
from until_functions.exceptions import getInput
from until_functions.grafic_interface import mensage
from Menu.Menu import Menu
from Menu.UserMenu import UserMenu


class MainMenu(Menu, ABC):

    def __init__(self):
        self.__methods = [None, self.creatAccount, self.login]
        self.__methods_name = ["Void", "Criar conta", "Fazer login"]

    def showMenu(self):
        for i in range(1, len(self.__methods)):
            print("({}) {}".format(i, self.__methods_name[i]))
        print("(-1) Para sair")

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
        while True:
            agency_number = getInput("Entre com o numero da sua agencia - entre 100 e 999\n=>", int, range(100, 1000))
            if agency_number != -100:
                break
        new_user = Account(user_name, password, account_number, agency_number)
        users[user_name] = new_user
        mensage("Usuário criado com sucesso")

    @staticmethod
    def login():
        user_name = getInput("Entre com o nome de usuário\n=>", str)
        if user_name not in users:
            print("Usuário não encontrado")
            return
        user = users[user_name]
        password = getInput("Entre com a senha\n=>", str)
        if password != user.getPassword():
            print("Senha incorreta")
            return
        mensage("Bem vindo {}".format(user_name))
        user.historic.addHistoric(getDay(), "Criação da conta")
        menu = UserMenu(user)

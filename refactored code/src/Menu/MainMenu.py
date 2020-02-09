from abc import ABC
from src.until_functions.data_base import users, getDay
from random import randrange
from src.Accounts.Account import Account
from src.until_functions.exceptions import getInput
from src.until_functions.grafic_interface import mensage
from src.Menu.Menu import Menu
from src.Menu.UserMenu import UserMenu


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
        new_user.historic.addHistoric(getDay(), "Criação da conta")
        mensage("Usuário criado com sucesso")

    @staticmethod
    def login():

        def validatePassword(password, user):
            return True if password is user.getPassword() else False

        def validateUsername(username):
            return users[username] if username in users else None

        user_name = getInput("Entre com o nome de usuário\n=>", str)
        user = validateUsername(user_name)
        if user is None:
            print('Nome de usuário inválido')
            return
        password = getInput("Entre com a senha\n=>", str)
        if validatePassword(password, user):
            mensage("Bem vindo {}".format(user_name))
            menu = UserMenu(user)
        else:
            print("Senha invalida")
            return

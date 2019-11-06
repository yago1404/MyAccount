# -*- coding: utf-8 -*-
__author__ = "Yago Taveiros"
__copyright__ = "Copyright 2019, by Taveiros"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "Yago Taveiros"
__email__ = "ytf@ic.ufal.br"
__status__ = "Prototype"

from random import randrange
from src.acount import Account

"""
Usuário atual da aplicação
"""
user = None # type: Account
"""
Dia atual
"""
day = 1  # type: int
"""
Dicionário de usuarios onde:
user name : user object
"""
users = {}

""" Retorna opção escolhida pelo usuário
recebe a entrada até um inteiro
retorna uma opção inteira 
"""
def getIntInput(text):
    while True:
        try:
            option = int(input(text))
        except ValueError:
            print("Insira um valor inteiro")
        else:
            break

    return option

def depose():
    global user  # type: Account
    value = getIntInput("Entre com o valor do deposito\n=>")
    user.depose(value)
    print("Saldo atual {}".format(user.getBalance()))


def dellAccount():
    global users
    global user
    option = input("Deseja realmente apagar sua conta?\n(sim)(nao)")
    if option == "sim":
        users.pop(user.getLogin())
        print("Conta apagada com sucesso")
        return True
    elif option == "nao":
        return False
    else:
        print("Entrada invalida\nOperação cancelada")
        return False


def addExpense():
    global user  # type: Account
    fixed_payment = user.getFixedPayments()
    print(fixed_payment)



def userMenu():
    while True:
        option = getIntInput("(1) Fazer deposito\n(2) Adicionar despesa\n(100) Apagar sua conta\n(-1) Sair\n=>")
        if option is 1:
            depose()

        elif option is 2:
            addExpense()

        elif option is 100:
            check = dellAccount()
            if check:
                return
        elif option is -1:
            return



def creatAccount():
    global users
    password = ""
    while True:
        user_name = input("Entre com o nome de usuario\n=>")
        if user_name in users:
            print("Esse usuário ja existe\nSelecione outro nome de usuário")
            continue
        password = input("Entre com a senha desejada\n=>")  # type: str
        break

    account_number = randrange(10000, 99999)
    print("O número da sua conta é: {}".format(account_number))

    agency_number = getIntInput("Entre com o numero da sua agencia\n=>")

    new_user = Account(user_name, password, account_number, agency_number)

    users[user_name] = new_user



def login():
    global users
    global user
    user_name = input("Entre com o nome de usuário\n=>")  # type: str
    if user_name not in users:
        print("Usuario não existe")
        return
    aux = users[user_name]  # type: Account
    password = input("Entre com a senha\n=>")
    if password == aux.getPassword():
        user = aux
        userMenu()
    else:
        print("Senha invalida")

    return


def main():
    print("My Banck\nMain Menu:")
    while True:
        option = getIntInput("(1) Criar Conta\n(2) Fazer Login\n(-1) Para sair\n=>")
        if option is -1:
            break
        elif option is 1:
            creatAccount()
        elif option is 2:
            login()


if __name__ == '__main__':
    main()

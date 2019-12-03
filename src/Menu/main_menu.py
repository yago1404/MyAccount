from until_functions.exceptions import getInput
from until_functions.grafic_interface import line
from until_functions.creat_functions import creatAccount
from Accounts.data_base import user


def teste():
    print("Entrei")

def mainMenu():
    actions = [None, creatAccount, teste]
    line()
    while True:
        option = getInput("## (1) Criar Conta\n## (2) Fazer Login\n## (-1) Para sair\n=>", int)
        if option is -1:
            print("end")
            return
        elif option < -1 or option > 2:
            print("A entrada esta fora do intervalo")
            return

        actions[option]()
        print(user)
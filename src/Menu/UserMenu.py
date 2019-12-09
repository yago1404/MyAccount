from abc import ABC
from Menu.Menu import Menu
from until_functions.exceptions import getInput


class UserMenu(Menu, ABC):
    def __init__(self, user):
        self.__methods = [None, user.getAccountInfo, user.fixedPayment, user.paymentSchedule, user.historic_op, user.balance]
        self.__methods_name = ["Void",
                               "Obter infromações da conta",
                               "Opeções sobre os pagamentos fixos",
                               "Opções sobre os pagamentos agendados",
                               "Opções sobre o histórico",
                               "Opções sobre o saldo"]
        self.exec()

    def showMenu(self):
        for i in range(1, len(self.__methods)):
            print("({}) {}".format(i, self.__methods_name[i]))
        print("(-1) Para sair")

    def exec(self):
        while True:
            self.showMenu()
            option = getInput("Entre com a opção desejada\n=>", int, range(1, 6))

            if option == -1:
                return
            elif option != -100:
                self.__methods[option]()

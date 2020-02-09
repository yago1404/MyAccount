from abc import ABC
from src.Menu.Menu import Menu
from src.until_functions.exceptions import getInput
from src.until_functions.data_base import spendDay


class UserMenu(Menu, ABC):
    def __init__(self, user):
        self.__methods = [
            None,
            user.getAccountInfo,
            user.fixedPayment,
            user.paymentSchedule,
            user.historic_op,
            user.balance_op,
            user.changeData
        ]
        self.__methods_name = [
            "Void",
            "Obter infromações da conta",
            "Opeções sobre os pagamentos fixos",
            "Opções sobre os pagamentos agendados",
            "Opções sobre o histórico",
            "Opções sobre o saldo",
            "Adicionar/Alterar informações da conta",
            "Passar o dia"
        ]
        self.exec()

    def showMenu(self):
        for i in range(1, len(self.__methods)+1):
            print("({}) {}".format(i, self.__methods_name[i]))
        print("(-1) Para sair")

    def exec(self):
        while True:
            self.showMenu()
            option = getInput("Entre com a opção desejada\n=>", int, range(1, 8))

            if option == -1:
                return
            elif option != -100:
                if option == 7:
                    spendDay()
                    continue
                self.__methods[option]()

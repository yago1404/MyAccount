from until_functions.exceptions import getInput


class Balance:
    def __init__(self):
        self.__balance = 0  # type: float

    def incrementBalance(self, value=None):
        if value is None:
            value = getInput("Entre com o valor do despósito\n=>", float, range(1, 1000000000))
            self.__balance = value
        else:
            self.__balance += value

    def decrementBalance(self, value=None):
        if value is None:
            value = getInput("Entre com o valor de decremento\n=>", float, range(1, 1000000000))
            self.__balance -= value
        else:
            self.__balance -= value

    def getBalance(self):
        return self.__balance

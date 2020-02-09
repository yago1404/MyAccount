from src.until_functions.exceptions import getInput
from src.until_functions.data_base import users, getDay


class Balance:
    def __init__(self):
        self.__balance = 0  # type: float

    def incrementBalance(self, value=None):
        if value is None:
            value = getInput("Entre com o valor do deposito\n=>", float, range(1, 1000000000))
            self.__balance += value
        else:
            self.__balance += value

    def decrementBalance(self, value=None):
        if value is None:
            value = getInput("Entre com o valor de decremento\n=>", float, range(1, 1000000000))
            self.__balance -= value
        else:
            self.__balance -= value

    def getBalance(self):
        print("Saldo atual: R$ {}".format(self.__balance))
        return self.__balance

    def transfer(self):
        to_send = getInput("Entre com o usuário para quem deseja realizar a transferencia\n=>", str)
        if to_send not in users:
            print("Usuário não encontrado")
            return
        value = getInput("Entre com o valor da transferencia", float, range(1, 10000000))
        if value > self.__balance:
            print("Não a saldo suficiente")
            return
        self.decrementBalance(value)
        user_to_send = users[to_send]
        user_to_send.balance.incrementBalance(value)
        user_to_send.historic.addHistoric(
            getDay(),
            "Recebimento de transferencia bancária no valor de {}".format(value)
        )

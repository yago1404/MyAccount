from abc import abstractmethod


class Expense:
    """
    Classe abstrata para sub-classes de cobrança na aplicação

    """

    @abstractmethod
    def getPaymentSchedule(self):
        pass

    @abstractmethod
    def getSpecificPayment(self, day):
        pass

    @abstractmethod
    def setPayment(self, day, value):
        pass

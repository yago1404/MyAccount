from abc import abstractmethod


class Expense:

    @abstractmethod
    def getPaymentSchedule(self):
        pass

    @abstractmethod
    def getSpecificPayment(self, day):
        pass

    @abstractmethod
    def setPayment(self, day, value):
        pass

from abc import abstractmethod, ABCMeta


class Schedule:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getPaymentSchedule(self):
        pass

    @abstractmethod
    def getPaymentsDay(self, day):
        pass

    @abstractmethod
    def setPayment(self, day, value):
        pass

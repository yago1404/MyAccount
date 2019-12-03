from abc import abstractclassmethod


class Schedule:

    @abstractclassmethod
    def getPaymentSchedule(self):
        pass

    @abstractclassmethod
    def getSpecificPayment(self, day):
        pass

    @abstractclassmethod
    def setPayment(self, day, value):
        pass

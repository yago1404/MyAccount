from typing import Dict
from src.user import User
from src.fixed_payment import FixedPayment
from src.schedule_payment import PaymentSchedule


class Account(User):

    __historic = Dict[int, int]

    def __init__(self, login, password, acount_number, agency_number):
        super(Account, self).__init__(login, password)
        self.__acountNumber = acount_number
        self.__agencyNumber = agency_number
        self.paymentsSchedule = PaymentSchedule()  # type: PaymentSchedule
        self.fixedPayment = FixedPayment()  # type: FixedPayment
        self.__historic = {}
        self.__balance = 0

    def getBalance(self):
        return self.__balance

    def getFixedPayments(self):
        aux = self.fixedPayment
        return aux.getPaymentSchedule()

    def getPaymentSchedule(self):
        return self.paymentsSchedule.getPaymentSchedule()

    def getAgencyNumber(self):
        return self.__agencyNumber

    def getAcountNumber(self):
        return self.__acountNumber

    def getHistoric(self):
        return self.__historic

    def depose(self, dep):
        self.__balance += dep

    def setPaymentAgend(self, day: int, value: float):
        self.paymentsSchedule.setPayment(day, value)

    def setFixedPayment(self, day: int, value: float):
        self.fixedPayment.setPayment(day, value)

    def setHistoric(self, action, value):
        self.__historic[action] = value

    def replaceHistoric(self):
        self.__historic = {}

    def decreatBalance(self, value):
        self.__balance -= value
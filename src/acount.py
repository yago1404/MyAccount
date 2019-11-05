from typing import Dict
from src.user import User


class Account(User):
    __paymentsAgend = ...  # type: Dict[int, int]

    def __init__(self, login, password, acount_number, agency_number):
        super(Account, self).__init__(login, password)
        self.__acountNumber = acount_number
        self.__agencyNumber = agency_number
        self.__paymentsAgend = {}
        for i in range(1, 31):
            self.__paymentsAgend[i] = 0
        self.__fixedPayment = {}
        for i in range(1, 31):
            self.__fixedPayment[i] = 0
        self.__historic = {}
        self.__balance = 0

    def getBalance(self):
        return self.__balance

    def getFixedPayments(self):
        return self.__fixedPayment

    def getPaymentAgend(self):
        return self.__paymentsAgend

    def getAgencyNumber(self):
        return self.__agencyNumber

    def getAcountNumber(self):
        return self.__acountNumber

    def getHistoric(self):
        return self.__historic

    def deposit(self, dep):
        self.__balance += dep

    def setPaymentAgend(self, day: int, value: float):
        if day is 0:
            day = 1
        self.__paymentsAgend[day] += value

    def setHistoric(self, action, value):
        self.__historic[action] = value

    def replaceHistoric(self):
        self.__historic = {}

    def decreatBalance(self, value):
        self.__balance -= value

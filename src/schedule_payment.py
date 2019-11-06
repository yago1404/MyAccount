from src.Interface_expense import Expense
from abc import ABC


class PaymentSchedule(Expense, ABC):

    def __init__(self):
        self.__shedule = {}

    def getPaymentSchedule(self):
        return self.__shedule

    def getSpecificPayment(self, day):
        return self.__shedule[day]

    def setPayment(self, day: int, value: float):
        self.__shedule[day] += value

from src.Interface_expense import Expense
from abc import ABC


class PaymentSchedule(Expense, ABC):

    def __init__(self):
        self.__schedule = {}
        for i in range(0,31):
            self.__schedule[i] = 0

    def getPaymentSchedule(self):
        return self.__schedule

    def getSpecificPayment(self, day):
        return self.__schedule[day]

    def setPayment(self, day: int, value: float):
        self.__schedule[day] += value

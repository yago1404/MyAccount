from abc import ABC
from src.Interface_expense import Expense


class FixedPayment(Expense, ABC):

    def __init__(self):
        self.schedule = {}
        for i in range(0,30):
            self.schedule[i] = 0

    def getPaymentSchedule(self):
        return self.schedule

    def getSpecificPayment(self, day: int):
        return self.schedule[day]

    def setPayment(self, day: int, value: float):
        self.schedule[day] += value

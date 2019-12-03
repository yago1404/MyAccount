from abc import ABC
from Schedules.Schedule import Schedule


class Payment:
    def __init__(self, day, value):
        self.__day = day
        self.__value = value

    def getPayment(self):
        return [self.__day, self.__value]


class SchedulePayment(Schedule, ABC):
    def __init__(self):
        self.__schedule = []

    def setPayment(self, day, value):
        new_payment = Payment(day, value)
        self.__schedule.append(new_payment)

    def getPaymentSchedule(self):
        return self.__schedule

    def getSpecificPayment(self, day):
        for i in self.__schedule:
            if (i.getPayment())[0] is day:
                return (i.getPayment())[1]

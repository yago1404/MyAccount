from abc import ABC
from Schedules.Schedule import Schedule
from Schedules.Payment import Payment
from until_functions.exceptions import getInput


class SchedulePayment(Schedule, ABC):
    def __init__(self):
        self.__schedule = []

    def setPayment(self, day=None, value=None, recipient=None):
        day = getInput("Entre com o dia do pagamento\n=>", int, range(1, 31))
        if day == -100:
            return
        value = getInput("Entre com o valor do pagamento\n=>", float, range(1, 10000000))
        if value == -100:
            return
        if input("Deseja adicionar o destinatário?\n(sim)(nao)=>") == "sim":
            recipient = input("Entre com o nome/código do destinatário")
        new_payment = Payment(day, value, recipient)
        self.__schedule.append(new_payment)

    def getPaymentSchedule(self):
        return self.__schedule

    def getPaymentsDay(self, day=None):
        if day is None:
            day = getInput("Entre com o dia\n=>", int, range(1, 31))
        last = []
        for i in self.__schedule:
            if (i.getPayment())[0] is day:
                last.append((i.getPayment())[1])

        return last

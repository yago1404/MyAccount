from abc import ABC
from src.Schedules.Schedule import Schedule
from src.Schedules.Payment import Payment
from src.until_functions.exceptions import getInput


class SchedulePayment(Schedule, ABC):
    def __init__(self):
        self.schedule = []

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
        self.schedule.append(new_payment)

    def getPaymentSchedule(self):
        for i in self.schedule:
            print(i)
        return self.schedule

    def getPaymentsDay(self, day=None):
        if day is None:
            day = getInput("Entre com o dia\n=>", int, range(1, 31))
        last = []
        for i in self.schedule:
            if (i.getPayment())[0] is day:
                last.append(i)
        for i in last:
            print(i)
        return last

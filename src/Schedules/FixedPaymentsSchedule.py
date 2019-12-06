from abc import ABC
from Schedules.Schedule import Schedule
from Schedules.Payment import Payment
from until_functions.exceptions import getInput


class FixedPaymentSchedule(Schedule, ABC):
    def __init__(self):
        self.__schedule = []

    def getPaymentSchedule(self):
        return self.__schedule

    def setPayment(self, day=None, value=None, recipient=None):
        day = getInput("Entre com o dia desejado para adicionar o agamento fixo\n=>", int, [1, 31])
        value = getInput("Entre com o valor desejado\n=>", float, [1, float("inf")])
        op = getInput("Deseja adicionar um beneficiado?\n(sim)(nao)=>", str)
        if op == "sim":
            recipient = getInput("Digite o nome do beneficiado\n=>", str)
        new_payment = Payment(day, value, recipient)
        self.__schedule.append(new_payment)
        return True

    def getPaymentsDay(self, day=None):
        last = []
        for i in self.__schedule:
            if (i.getPayment())[0] is day:
                last.append((i.getPayment())[1])

        return last

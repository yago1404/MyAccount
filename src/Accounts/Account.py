from Accounts.User import User
from Schedules.FixedPaymentsSchedule import FixedPaymentSchedule
from Schedules.SchedulePayment import SchedulePayment
from Accounts.Historic import Historic
from Accounts.Balance import Balance
from until_functions.exceptions import getInput


class Account(User):
    def __init__(self, user_name, password, account_number, agency_number):
        super(Account, self).__init__(user_name, password)
        self.__agency_number = agency_number
        self.__account_number = account_number
        self.__fixed_payment = FixedPaymentSchedule()
        self.__payment_schedule = SchedulePayment()
        self.__historic = Historic()
        self.__balance = Balance()

    def getAccountNumber(self):
        return self.__account_number

    def getAgencyNumber(self):
        return self.__agency_number

    def fixedPayment(self):
        methods = [
            None,
            self.__fixed_payment.getPaymentSchedule,
            self.__fixed_payment.getPaymentsDay,
            self.__fixed_payment.setPayment
        ]
        option = getInput(
                "(1) Ver a agenda de pagamentos fixos\n"
                "(2) Ver os pagamentos de um dia especificos\n"
                "(3) Adicionar um pagamento para determinado dia\n"
                "(-1) Cancelar", int, range(1, 4)
            )
        if option is -1:
            print("Operação cancelada")
            return
        return methods[option]()

    def paymentSchedule(self):
        methods = [
            None,
            self.__payment_schedule.setPayment,
            self.__payment_schedule.getPaymentSchedule,
            self.__payment_schedule.getPaymentsDay
        ]
        option = getInput(
            "(1) Agendar um pagamento\n"
            "(2) Exibir agenda de pagamentos\n"
            "(3) Exibir pagamentos de um dia específico\n"
            "(-1) sair\n"
            "=>", int, range(1,4)
        )

        if option is -100:
            print("Operação cancelada")
            return
        else:
            methods[option]()

    def getHistoric(self):
        return self.__historic.getHistoric()

    def getBalance(self):
        return self.__balance.getBalance()

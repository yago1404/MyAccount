from src.Accounts.User import User
from src.Schedules.FixedPaymentsSchedule import FixedPaymentSchedule
from src.Schedules.SchedulePayment import SchedulePayment
from src.Accounts.Historic import Historic
from src.Accounts.Balance import Balance
from src.until_functions.exceptions import getInput
from src.until_functions.grafic_interface import mensage
from src.until_functions.data_base import getDay



class Account(User):
    def __init__(self, user_name, password, account_number, agency_number):
        super(Account, self).__init__(user_name, password)
        self.__agency_number = agency_number
        self.__account_number = account_number
        self.fixed_payment = FixedPaymentSchedule()
        self.payment_schedule = SchedulePayment()
        self.historic = Historic()
        self.balance = Balance()

    def getAccountNumber(self):
        return self.__account_number

    def getAgencyNumber(self):
        return self.__agency_number

    def fixedPayment(self):
        methods = [
            None,
            self.fixed_payment.getPaymentSchedule,
            self.fixed_payment.getPaymentsDay,
            self.fixed_payment.setPayment
        ]
        option = getInput(
                "(1) Ver a agenda de pagamentos fixos\n"
                "(2) Ver os pagamentos de um dia especificos\n"
                "(3) Adicionar um pagamento para determinado dia\n"
                "(-1) Cancelar\n"
                "entre com a opção desejada\n=>",
                int,
                range(1, 4)
            )
        if option is -1:
            print("Operação cancelada")
            return
        if option != -100:
            if option == 3:
                self.historic.addHistoric(getDay(), "Despesa adicionada")
            return methods[option]()

    def paymentSchedule(self):
        methods = [
            None,
            self.payment_schedule.setPayment,
            self.payment_schedule.getPaymentSchedule,
            self.payment_schedule.getPaymentsDay
        ]
        option = getInput(
            "(1) Agendar um pagamento\n"
            "(2) Exibir agenda de pagamentos\n"
            "(3) Exibir pagamentos de um dia específico\n"
            "(-1) sair\n"
            "=>", int, range(1, 4)
        )

        if option is -1:
            print("Operação cancelada")
            return
        if option != -100:
            if option == 1:
                self.historic.addHistoric(getDay(), "Despesa adicionada")
            methods[option]()

    def historic_op(self):
        methods = [
            None,
            self.historic.clearHistoric,
            self.historic.getHistoricDay,
            self.historic.showHistoric
        ]
        option = getInput(
            "(1) Limpar o historico\n"
            "(2) Exibir histórico de um dia específico\n"
            "(3) Exibir histórico do mês\n"
            "(-1) Cancelar\n"
            "entre com a opção desejada\n=>",
            int,
            range(1, 4)
        )
        if option is -1:
            print("Operação cancelada")
            return
        if option != -100:
            return methods[option]()

    def balance_op(self):
        methods = [
            None,
            self.balance.incrementBalance,
            self.balance.getBalance,
            self.balance.transfer
        ]
        option = getInput(
            "(1) Realizar depósito\n"
            "(2) Mostrar saldo\n"
            "(3) Realizar transferencia\n"
            "(-1) Cancelar\n"
            "Entre com a opção desejada\n=>",
            int,
            range(1, 4)
        )
        if option is -1:
            print("Operação cancelada")
            return
        if option != -100:
            if option == 1:
                self.historic.addHistoric(getDay(), "Deposito realizado")
            elif option == 3:
                self.historic.addHistoric(getDay(), "transferencia realizada")
            return methods[option]()

    def getAccountInfo(self):
        mensage(
            "Nome de usuário: {}\n"
            "Saldo: {}\n"
            "Numero da conta: {}\n"
            "Endereço: {}\n"
            "Agencia bancária: {}\n"
            "Numero do telefone: {}\n"
            "Email: {}\n"
            "Genero: {}"
            .format(
                self.getLogin(),
                self.balance.getBalance(),
                self.getAccountNumber(),
                self.getAddress(),
                self.getAgencyNumber(),
                self.getCellphone(),
                self.getEmail(),
                self.getGenre()
            )
        )

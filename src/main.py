from random import randrange
from src.acount import Account

day = 1  # type: int
users = []


def spendDay():
    global day
    day += 1
    day %= 31
    if day is 0:
        day += 1

    print("Dia de hoje: Dia {}".format(day))


def thisUserExiste(user_name):
    for i in users:
        if i.getLogin() == user_name:
            return True

    return False


def thisAcountNumberExiste(acount_number):
    for i in users:
        if i.getAcountNumber == acount_number:
            return True

    return False


def creatAcount():
    existe = True
    user_name = ""
    acount_number = ""
    while existe:
        user_name = input("Entre com o nome de usuário que deseja\n=> ")
        existe = thisUserExiste(user_name)
        if existe:
            print("Nome de usuário ja existe")

    password = input("Entre com a senha desejada\n=> ")

    existe = True
    while existe:
        acount_number = str(randrange(100000, 999999))
        existe = thisAcountNumberExiste(acount_number)

    print("O numero da sua conta é\n=> {}".format(acount_number))

    agency = input("Entre com o nome da sua agencia bancaria\n=> ")

    new_acount = Account(user_name, password, acount_number, agency)

    users.append(new_acount)


def login():
    user = ""
    confirm = False  # type: bool
    while not confirm:
        user = input("Entre com o nome do ususario\n=> ")
        confirm = thisUserExiste(user)
        if not confirm:
            print("Esse usuario não existe")

    u = None
    for i in users:
        if i.getLogin() == user:
            u = i
            break

    confirm = True
    while confirm:
        password = input("entre com a senha\n=> ")
        if password == u.getPassword():
            break

        print("Senha invalida. Tente novamente")

    return [True, u]


def bankDeposit(user):
    global day
    while True:
        try:
            to_deposti = float(input("Entre com o valor do depostio"))  # type: float

        except ValueError:
            print("Entrada invalida. Entre com o valor correto")
        else:
            break

    user.deposit(to_deposti)
    user.setHistoric("Deposito bancario no dia {}".format(str(day)), to_deposti)


def showUserInformation(user):
    """

    :type user: Account
    """
    print("Nome de usuario: {}\n"
          "Saldo da conta: {}\n"
          "Pagamentos fixos: {}\n"
          "Pagamentos agendados: {}\n"
          "Agencia: {}\n"
          "Numero da conta: {}\n"
          "Histórico: {}\n"
          .format(user.getLogin(),
                  user.getBalance(),
                  user.getFixedPayments(),
                  user.getPaymentAgend(),
                  user.getAgencyNumber(),
                  user.getAcountNumber(),
                  user.getHistoric()
                  )
          )


def addFixedPayment(user: Account):
    while True:
        try:
            day_to_payment = int(input("Entre com o dia da despesa\n=> "))  # type: int
        except ValueError:
            print("Entrada invalida")
        else:
            if day_to_payment > 30 or day_to_payment < 1:
                print("Impossivel de realizar a operação\nData invalida")
                return

            break

    while True:
        try:
            value = float(input("Entre com o valor da despesa"))  # type: float
        except ValueError:
            print("Entrada invalida")
        else:
            break

    user.setPaymentAgend(day_to_payment, value)


def getNextDay():
    global day
    new_day = (day + 1) % 31  # type: int
    if new_day == 0:
        return 1

    return new_day


def checkSchedule(user):
    global day
    fixed_payment = user.getFixedPayments()
    if fixed_payment[day] > 0:

        if user.getBalance() >= fixed_payment[day]:
            user.decreaseBalance(fixed_payment[day])
            print("Pagamento realizado no valor de {}".format(fixed_payment[day]))

        else:
            print("Slado insuficiente\nPagamento adiado para dia {}".format(str(getNextDay())))
            user.setPaymentAgend((day + 1) % 31, fixed_payment[day])


def accomplishPayment(user):
    global day
    code = input("Entre com o codigo do boleto")  # type: str

    while True:
        try:
            value = int(input("Entre com o valor do boleto\n=>"))
        except ValueError:
            print("Entrada invalida, entre com um valor inteiro")
        else:
            break

    if user.getBalance() < value:
        print("Impossivel de realizar a operação\n"
              "saldo insuficiente")
        return

    user.setHistoric("Pagamento do boleto {} no dia {}".format(code, day), value)
    user.deposit((-1) * value)


def schedulePayment(user):
    while True:
        try:
            day_to_pay = int(input("Entre com o dia para o pagamento\n=>"))  # type: int
        except ValueError:
            print("Entrada invalida")
        else:
            if day_to_pay > 30 or day_to_pay < 1:
                print("Dia invalido")
            else:
                break

    while True:
        try:
            value = int(input("Entre com o valor do pagamento\n=>"))  # type: int
        except ValueError:
            print("Entrada invalida, insira um valor interio")
        else:
            break

    user.setPaymentAgend(day_to_pay, value)


def userMenu(user):
    """

    :type user: Account
    """
    is_user = True  # type: bool
    while is_user:
        while True:
            try:
                option = int(input("(1) Fazer deposito\n"
                                   "(2) Adicionar despesa\n"
                                   "(3) Realizar pagamento de boleto\n"
                                   "(4) Agendar pagamento\n"
                                   "(5) alterara dados da conta\n"
                                   "(6) Exibir informações da conta\n"
                                   "(7) Realizar tranferencia\n"
                                   "(8) Logout\n"
                                   "(9) Consultar historico\n"
                                   "(10) Passar o dia\n=> "))

            except ValueError:
                print("Entrada invalida")

            else:
                break

        if option == 1:
            bankDeposit(user)

        elif option == 2:
            addFixedPayment(user)

        elif option == 3:
            accomplishPayment(user)

        elif option == 4:
            schedulePayment(user)

        elif option == 6:
            showUserInformation(user)

        elif option == 8:
            is_user = False

        elif option is 10:
            spendDay()
            if day is 1:
                user.replaceHistoric()
            checkSchedule(user)


def mainMenu():
    global day
    print("Entre com a opção desejada")
    verify = True
    option = -1
    while verify:
        try:
            print("(1) Criar conta\n"
                  "(2) Logar\n"
                  "(3) Passar dia\n"
                  "(-1) sair")
            option = int(input("=> "))
        except ValueError:
            print("Entrada invalida\nPor favor entre com um valor inteiro:")
        else:
            verify = False

    if option == 1:
        creatAcount()
    elif option == 2:
        log = login()
        if log[0]:
            print("Bem vindo {}".format(log[1].getLogin()))
            userMenu(log[1])
    elif option == 3:
        spendDay()

    return option


def main():
    print("Bem vindo ao MyBank")
    option = 0
    while option != -1:
        option = mainMenu()

    print("Fim dos processos")


if __name__ == '__main__':
    main()

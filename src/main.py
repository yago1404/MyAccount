# -*- coding: utf-8 -*-

"""
    Este programa busca implementar uma solução para um administrador de conta bancaria, que simultneamente
tem um gerenciamento de históricos e agendas de pagamentos, onde ao passar de cada dia é verificado se
o usuário logado na aplicação tem pagamentos pendentes para esse dia - seja em qualquer uma das agendas

    A cada execução de paamento nescessária, o sistema verifica se o usuário tem saldo o suficiente para
realizar determinada operação, onde caso não seja possivel o sistema adia o pagamento em um dia e adiciona-o 
a agenda de pagamentos agendados

    No historico temos por padrão:
        acao "index da acao" no dia "dia" : "Acao"
"""

__author__ = "Yago Taveiros"
__copyright__ = "Copyright 2019, by Taveiros"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.0.0"
__maintainer__ = "Yago Taveiros"
__email__ = "ytf@ic.ufal.br"
__status__ = "Prototype"

from random import randrange
from src.account import Account

"""
Usuário atual da aplicação
"""
user = Account(None, None, None, None)  # type: Account
"""
Dia atual
"""
day = 1  # type: int
"""
Dicionário de usuarios onde:
user name : user object
"""
users = {}


""" Retorna opção escolhida pelo usuário
recebe a entrada até um inteiro
retorna uma opção inteira 
"""


def addToHistoric(action):
    global user, day
    action_of_the_day = user.getAction()
    user.setHistoric("Dia {} acao {}".format(day, action_of_the_day), action)
    action_of_the_day += 1


def getInput(text, value_type):
    while True:
        try:
            option = value_type(input(text))
        except ValueError:
            print("Insira um valor valido")
        else:
            break

    return option


def depose():
    global user  # type: Account
    value = getInput("Entre com o valor do deposito\n=>", float)  # type: float

    user.depose(value)
    print("Saldo atual {}".format(user.getBalance()))

    addToHistoric("Depósito no valor de {}".format(value))


def dellAccount():
    global users
    global user
    option = input("Deseja realmente apagar sua conta?\n(sim)(nao)")
    if option == "sim":
        users.pop(user.getLogin())
        print("Conta apagada com sucesso")
        return True
    elif option == "nao":
        return False
    else:
        print("Entrada invalida\nOperação cancelada")
        return False


def addExpense():
    global user  # type: Account
    day_to_expende = getInput("Entre com o dia que deseja adicionar a despesa\n=> ", int)
    if day_to_expende > 30 or day_to_expende < 1:
        print("Dia invalido")
        return
    value = getInput("Entre com o valor da despesa\n=>", float)
    user.fixedPayment.schedule[day_to_expende] = value
    addToHistoric("Despesa adicionada para dia {} no valor de {}".format(day_to_expende, value))


def checkExpense(value) -> bool:
    global user
    if user.getBalance() > value:
        return True
    return False


def makePayment():
    global user
    billet_code = getInput("Entre com o codigo do boleto\n=> ", str)
    value = getInput("Entre com o valor do boleto\n=> ", float)  # type: float
    if not checkExpense(value):
        print("Saldo insuficiente para o pagamento")
        return
    user.decreatBalance(value)
    addToHistoric("Pagamento do boleto {} no de valor {}".format(billet_code, value))
    print("Pagamento realizado com sucesso\nSaldo atual {}".format(user.getBalance()))


def schedulePayment():
    global user
    day_to_event = getInput("Entre com o dia que deseja agendar o pagamento\n=> ", int)
    if day_to_event > 30 or day_to_event < 1:
        print("Dia invalido")
        return
    value = getInput("Entre com o valor do pagamento\n=>", float)
    user.paymentsSchedule.setPayment(day_to_event, value)
    addToHistoric("Pagamento agendado para dia {} no valor de {}".format(day_to_event, value))


def changeData():
    global user, users
    user_name = user.getLogin()
    methods = [None, user.setLogin, user.setPassword, user.setGenre, user.setEmail, user.setCellphone, user.setAdress]
    print(
        "(1) Mudar login\n"
        "(2) Mudar senha\n"
        "(3) Mudar genero\n"
        "(4) Mudar E-mail\n"
        "(5) Mudar telefone\n"
        "(6) Mudar endereço\n"
        "(-1) Para cancelar"
    )
    option = getInput("=>", int)
    if option is -1:
        return
    new_data = getInput("Entre com o novo dado\n=> ", str)
    if option is 1:
        if new_data in users:
            print("Este nome de usuario ja existe")
            return
        aux = users[user_name]
        users.pop(user_name)
        users[new_data] = aux
    methods[option](new_data)
    addToHistoric("Alteração dos dados do usuario")


def displayData():
    global user
    print(
        "Usuário: {}\n"
        "Numero da conta: {}\n"
        "Agencia bancaria{}\n"
        "Saldo: {}\n"
        "Genero: {}\n"
        "E-mail: {}\n"
        "Numero do calular: {}\n"
        "Endereço: {}\n"
            .format(
            user.getLogin(),
            user.getAccountNumber(),
            user.getAgencyNumber(),
            user.getBalance(),
            user.getGenre(),
            user.getEmail(),
            user.getCellphone(),
            user.getAdress()
        )
    )


def displayHistoric():
    global user
    hist = user.getHistoric()
    print(hist)


def displayPaymentSchedule():
    global user
    schedule = user.getPaymentSchedule()
    for key in schedule:
        if schedule[key] is not 0:
            print("Dia {}, Valor: R${}".format(key, schedule[key]))


def displayFixedPayment():
    global user
    schedule = user.getFixedPayments()
    for key in schedule:
        if schedule[key] is not 0:
            print("Dia {}, Valor: R${}".format(key, schedule[key]))


def bankTransfer():
    global user
    global users
    action_of_the_day = user.getAction()
    save = user
    user_to_transfer = getInput("Entre com o nome do usuario para quem deseja realizar a trnaferencia bancaria\n=>",
                                str)
    if user_to_transfer not in users:
        print("Usuário não encontrado")
        return
    other_user = users[user_to_transfer]  # type: Account
    value = getInput("Entre com o valor do deposito\n=>", float)
    if user.getBalance() >= value:
        user.decreatBalance(value)
        other_user.depose(value)
        user = other_user
        addToHistoric("Recebimento de tranferencia bancaria no valor de {}".format(value))
        action_of_the_day -= 1
        user = save
        print("Operação realizada com sucesso")
        addToHistoric("Transferencia bancaria no valor de {}, para o usuário {}".format(value, user_to_transfer))
    else:
        print("Saldo insuficiente para realizar essa operação")


def spendDay():
    global users, user, day

    def checkPaymentSchedule():
        schedule = user.getPaymentSchedule()
        if schedule[day] > user.getBalance():
            print("Impossível de efetuar os pagamentos agendados")
        else:
            if schedule[day] is 0:
                print("Não a pagamentos agendados para hoje")
                return
            user.decreatBalance(schedule[day])
            user.paymentsSchedule.clearPayment(day)
            print("Pagamento agendado efetuado com sucesso")

    def checkFixedPayment():
        schedule = user.getFixedPayments()
        if schedule[day] > user.getBalance():
            print("Impossível de efetuar os pagamentos fixos desse dia\nPagamentos adiados para dia {}".format((day + 7) % 31))
            user.setPaymentAgend(day + 7, schedule[day])
        else:
            if schedule[day] is 0:
                print("Não a pagamentos fixos para o dia de hoje")
                return
            user.decreatBalance(schedule[day])
            print("Pagamento fixo de hoje efetuado com sucesso")

    day = (day + 1) % 31
    user.setAction(1)
    if day is 0:
        day += 1
        user.clearHistoric()
    checkFixedPayment()
    checkPaymentSchedule()
    print("Dia de hoje: {}".format(day))


def userMenu():
    global user
    functions = [None,
                 depose,
                 addExpense,
                 makePayment,
                 schedulePayment,
                 changeData,
                 displayData,
                 displayHistoric,
                 displayPaymentSchedule,
                 displayFixedPayment,
                 bankTransfer,
                 spendDay
                 ]
    while True:
        option = getInput(
            "(1) Fazer deposito\n"
            "(2) Adicionar despesa\n"
            "(3) Para realizar pagamento\n"
            "(4) Agendar pagamento\n"
            "(5) Alterar/Adicionar dados da conta\n"
            "(6) Exibir informações da conta\n"
            "(7) Exibir hitórico\n"
            "(8) Exibir agenda de pagamentos\n"
            "(9) Exibir pagamentos fixos\n"
            "(10) Realizar transferência\n"
            "(11) Passar dia\n"
            "(-1) Sair\n=>",
            int
        )
        if option is -1:
            user = None
            return
        try:
            functions[option]()
        except IndexError:
            print("Entrada invalida")


def creatAccount():
    global users
    password = ""
    while True:
        user_name = input("Entre com o nome de usuario\n=>")
        if user_name in users or user_name is "":
            print("Esse usuário ja existe ou esse nome é invalido\nSelecione outro nome de usuário")
            continue
        password = input("Entre com a senha desejada\n=>")  # type: str
        break

    account_number = randrange(10000, 99999)
    print("O número da sua conta é: {}".format(account_number))
    agency_number = getInput("Entre com o numero da sua agencia\n=>", int)
    new_user = Account(user_name, password, account_number, agency_number)
    users[user_name] = new_user


def login():
    global users
    global user
    user_name = input("Entre com o nome de usuário\n=>")  # type: str
    if user_name not in users:
        print("Usuario não existe")
        return
    aux = users[user_name]  # type: Account
    password = input("Entre com a senha\n=>")
    if password == aux.getPassword():
        user = aux
        userMenu()
    else:
        print("Senha invalida")

    return


def main():
    print("My Banck\nMain Menu:")
    functions = [None, creatAccount, login]
    while True:
        option = getInput("(1) Criar Conta\n(2) Fazer Login\n(-1) Para sair\n=>", int)
        if option is -1:
            break
        try:
            functions[option]()
        except IndexError:
            print("Insira um valor dentro do intervalo ou -1 para sair")
        except TypeError:
            print("Insira um valor dentro do intervalo ou -1 para sair")


if __name__ == '__main__':
    main()

from src.until_functions.grafic_interface import mensage


users = {}
day = 1


def spendDay():
    global day
    day = (day + 1) % 31
    if day == 0:
        day += 1
        for i in users:
            users[i].historic.clearHistoric()
    for i in users:
        user = users[i]
        for j in user.fixed_payment.schedule:
            if j.day == getDay():
                if j.value <= user.balance.getBalance():
                    user.balance.decrementBalance(j.value)
                    print("Pagamento efetuado com sucesso")
                else:
                    print("Impossivel efetuar o pagamento")
    for i in users:
        user = users[i]
        for j in user.payment_schedule.schedule:
            if j.day == getDay():
                if j.value <= user.balance.getBalance():
                    user.balance.decrementBalance(j.value)
                    print("Pagamento efetuado com sucesso")
                else:
                    print("Impossivel efetuar o pagamento")
        if day == 1:
            for k in users:
                users[k].payment_schedule.schedule = []
    mensage("Dia de hoje: {}".format(day))


def getDay():
    global day
    return day

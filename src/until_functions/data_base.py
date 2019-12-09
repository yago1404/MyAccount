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
    """
        TODO: implementar check list de pagamentos
    """
    mensage("Dia de hoje: {}".format(day))


def getDay():
    global day
    return day

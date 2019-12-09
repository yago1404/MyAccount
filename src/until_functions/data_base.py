users = {}
day = 1


def spendDay():
    global day
    day += 1
    print("Dia de hoje: {}".format(day))


def getDay():
    global day
    return day

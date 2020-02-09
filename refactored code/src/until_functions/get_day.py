from src.until_functions.exceptions import getInput


def getPaymentsDay(obj, day=None):
    if day is None:
        day = getInput("Entre com o dia\n=>", int, range(1, 31))
    last = []
    for i in obj.schedule:
        if (i.getPayment())[0] is day:
            last.append(i)
    for i in last:
        print(i)
    return last


def getInputDay():
    day = getInput("Entre com o dia que deseja\n=>", int, range(1, 31))
    return day

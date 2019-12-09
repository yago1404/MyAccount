from src.until_functions.exceptions import getInput


def getInputDay():
    day = getInput("Entre com o dia que deseja\n=>", int, range(1, 31))
    return day
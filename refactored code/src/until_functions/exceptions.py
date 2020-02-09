def getInput(text, value_type, interval=None):
    if interval is None:
        interval = [0]
    while True:
        try:
            option = value_type(input(text))
        except ValueError:
            print("Insira um valor valido")
        else:
            break

    if value_type is int and option not in interval and (option != -1):
        print("O valor esta fora do intervalo de {} a {}".format(min(interval), max(interval)))
        return -100

    return option

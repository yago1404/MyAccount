
def getInput(text, value_type):
    while True:
        try:
            option = value_type(input(text))
        except ValueError:
            print("Insira um valor valido")
        else:
            break

    return option
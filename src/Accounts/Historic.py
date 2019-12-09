from until_functions.get_day import getInputDay
from until_functions.exceptions import getInput


class Historic:
    def __init__(self):
        self.__historic = []

    def getHistoric(self):
        return self.__historic

    def getHistoricDay(self, day=None):
        if day is None:
            day = getInputDay()
        last = []
        for i in self.__historic:
            if i[0] is day:
                last.append(i[1])
        for i in last:
            print(i)

    def addHistoric(self, day=None, action=None):
        if day is None:
            day = getInputDay()
        if action is None:
            action = getInput("Entre com a ação", str)
        new_action = [day, action]
        self.__historic.append(new_action)
        self.__historic = sorted(self.__historic)

    def clearHistoric(self):
        self.__historic = []

    def showHistoric(self):
        for i in self.__historic:
            print("Dia {}:\n    {}".format(i[0], i[1]))

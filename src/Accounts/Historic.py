from until_functions.get_day import getInputDay


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
                last.append(i)
        return last

    def addHistoric(self, day=None, action=None):
        if day is None:
            day = getInputDay()
        new_action = [day, action]
        self.__historic = sorted(self.__historic.append(new_action))

    def clearHistoric(self):
        self.__historic = []

    def showHistoric(self):
        for i in self.__historic:
            print("Dia {}:\n    {}".format(i[0], i[1]))

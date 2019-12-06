class Payment:
    def __init__(self, day, value, recipient=None):
        self.__day = day
        self.__value = value
        if recipient is None:
            recipient = "Indefinido"
        self.__recipient = recipient

    def getPayment(self):
        return [self.__day, self.__value, self.__recipient]

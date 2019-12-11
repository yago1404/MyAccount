class Payment:
    def __init__(self, day, value, recipient=None):
        self.day = day
        self.value = value
        if recipient is None:
            recipient = "Indefinido"
        self.__recipient = recipient

    def __str__(self):
        return "\n\nDia :{}\nValor: {}\nDestinatário {}\n\n".format(self.day, self.value, self.__recipient)

    def getPayment(self):
        return [self.day, self.value, self.__recipient]

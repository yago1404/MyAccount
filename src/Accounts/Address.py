class Address:
    def __init__(self, address):
        self.__address = address

    def checkAddress(self):
        if self.__address.find("Av.") or self.__address.find("Rua"):
            return True
        else:
            return False

    def setAddress(self, new_data):
        self.__address = new_data

    def getAddress(self):
        return self.__address

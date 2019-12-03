class CellPhone:
    def __init__(self, cellphone):
        self.__number = cellphone

    def checkCellPhone(self):
        if len(self.__number) is 9:
            return True
        else:
            return False

    def setNumber(self, new_data):
        self.__number = new_data

    def getNumber(self):
        return self.__number

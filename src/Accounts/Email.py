class Email:
    def __init__(self, data):
        self.__email = data

    def __str__(self):
        return "{}".format(self.__email)

    def checkEmail(self):
        if self.__email.find("@") and self.__email.find(".com") and self.__email[0] != "@":
            return True
        else:
            return False

    def getEmail(self):
        return self.__email

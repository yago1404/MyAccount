from Accounts.Email import Email
from Accounts.CellPhone import CellPhone


class User:

    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__genre = "Indefinido"
        self.__email = "Indefinido"
        self.__cellphone = "Indefinido"
        self.__address = "Indefinido"

    def getPassword(self):
        return self.__password

    def getLogin(self):
        return self.__login

    def getGenre(self):
        return self.__genre

    def getEmail(self):
        return self.__email.getEmail()

    def getCellphone(self):
        return self.__cellphone.getNumber()

    def getAddress(self):
        return self.__address.getAddress()

    def setPassword(self, new_password):
        self.__password = new_password
        print("Senha alterada com sucesso")

    def setLogin(self, new_login):
        self.__login = new_login
        print("Login alterado com sucesso")

    def setGenre(self, new_data):
        self.__genre = new_data

    def setEmail(self, new_data):
        aux = Email(new_data)
        if aux.checkEmail():
            self.__email = aux
        else:
            print("Erro ao tentar alterar o email\nverifique se informou o email correto")

    def setCellphone(self, new_data):
        self.__cellphone = CellPhone(new_data)

    def setAddress(self, new_data):
        self.__address = new_data

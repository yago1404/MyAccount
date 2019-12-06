from Accounts.Email import Email
from Accounts.CellPhone import CellPhone
from until_functions.exceptions import getInput


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

    def setPassword(self, new_password=None):
        if new_password is None:
            new_password = getInput("Entre com a nova senha\n=>", str)
        if new_password == "":
            print("Impossivel alterar a senha\nSENHA VAZIA")
            return
        self.__password = new_password
        print("Senha alterada com sucesso")

    def setLogin(self, new_login=None):
        if new_login is None:
            new_login = getInput("Entre com a nova senha\n=>", str)
        if new_login == "":
            print("Impossivel alterar o login")
            return
        self.__login = new_login
        print("Login alterado com sucesso")

    def setGenre(self, new_data=None):
        if new_data is None:
            new_data = getInput("Entre com o genero\n=>")
        if new_data == "":
            print("Impossivel inserir novo dado")
            return
        self.__genre = new_data
        print("Genero alterado com sucesso")

    def setEmail(self, new_data):
        aux = Email(new_data)
        if aux.checkEmail():
            self.__email = aux
        else:
            print("Erro ao tentar alterar o email\nverifique se informou o email correto")

    def setCellphone(self, new_data):
        if len(new_data) != 11:
            print("Numero de telefone invalido")
            return
        self.__cellphone = CellPhone(new_data)
        print("Telefone alterado com sucesso")

    def setAddress(self, new_data):
        self.__address = new_data

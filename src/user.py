class User:

    def __init__(self, login, password):
        print("Iniciei o usuario")
        self.__login = login
        self.__password = password

    def getPassword(self):
        return self.__password

    def getLogin(self):
        return self.__login

    def setPassword(self, newPassword):
        self.__password = newPassword
        print("Senha alterada com sucesso")

    def setLogin(self, newLogin):
        self.__login = newLogin
        print("Login alterado com sucesso")

class User:

    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.genre = "Indefinido"
        self.email = "Indefinido"
        self.cellphone = "Indefinido"
        self.adress = "Indefinido"


    def getPassword(self):
        return self.__password

    def getLogin(self):
        return self.__login

    def getGenre(self):
        return self.genre

    def getEmail(self):
        return self.email

    def getCellphone(self):
        return self.cellphone

    def getAdress(self):
        return self.adress

    def setPassword(self, newPassword):
        self.__password = newPassword
        print("Senha alterada com sucesso")

    def setLogin(self, newLogin):
        self.__login = newLogin
        print("Login alterado com sucesso")

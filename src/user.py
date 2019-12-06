class User:

    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__genre = "Indefinido"
        self.__email = "Indefinido"
        self.__cellphone = "Indefinido"
        self.__adress = "Indefinido"

    def getPassword(self):
        return self.__password

    def getLogin(self):
        return self.__login

    def getGenre(self):
        return self.__genre

    def getEmail(self):
        return self.__email

    def getCellphone(self):
        return self.__cellphone

    def getAdress(self):
        return self.__adress

    def setPassword(self, new_password):
        self.__password = new_password
        print("Senha alterada com sucesso")

    def setLogin(self, new_login):
        self.__login = new_login
        print("Login alterado com sucesso")

    def setGenre(self, new_data):
        self.__genre = new_data

    def setEmail(self, new_data):
        self.__email = new_data

    def setCellphone(self, new_data):
        self.__cellphone = new_data

    def setAdress(self, new_data):
        self.__adress = new_data

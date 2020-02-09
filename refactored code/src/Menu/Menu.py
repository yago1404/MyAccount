from abc import abstractmethod


class Menu:

    @abstractmethod
    def showMenu(self):
        pass

    @abstractmethod
    def exec(self):
        pass

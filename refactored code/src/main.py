# -*- coding: utf-8 -*-
from src.Menu.MainMenu import MainMenu
from src.until_functions.grafic_interface import line


def main():
    line()
    print("##           Bem Vindo ao MyBank            ##")
    print("##            Versão: BETA 1.0.1            ##")
    line()
    a = MainMenu()
    a.exec()


if __name__ == "__main__":
    main()

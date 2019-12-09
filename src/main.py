# -*- coding: utf-8 -*-

"""
    Este programa busca implementar uma solução para um administrador de conta bancaria, que simultneamente
tem um gerenciamento de históricos e agendas de pagamentos, onde ao passar de cada dia é verificado se
o usuário logado na aplicação tem pagamentos pendentes para esse dia - seja em qualquer uma das agendas

    A cada execução de paamento nescessária, o sistema verifica se o usuário tem saldo o suficiente para
realizar determinada operação, onde caso não seja possivel o sistema adia o pagamento em um dia e adiciona-o
a agenda de pagamentos agendados

    No historico temos por padrão:
        acao "index da acao" no dia "dia" : "Acao"
"""

__author__ = "Yago Taveiros"
__copyright__ = "Copyright 2019, by Taveiros"
__credits__ = "Todos desenvolvedores de software livre"
__license__ = "GNU General Public License"
__version__ = "1.1.0"
__maintainer__ = "Yago Taveiros"
__email__ = "ytf@ic.ufal.br"
__status__ = "Prototype"

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

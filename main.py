# main.py

from view.view import InscricaoView
import os

def main():
    """
    Ponto de entrada do sistema.

    Princípios aplicados:
    - Modularidade: separa a execução principal da lógica de apresentação.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    view = InscricaoView()
    view.exibir_menu()

if __name__ == "__main__":
    main()
# main.py

from view.view import InscricaoView

def main():
    """
    Ponto de entrada do sistema.

    Princípios aplicados:
    - Modularidade: separa a execução principal da lógica de apresentação.
    """
    view = InscricaoView()
    view.exibir_menu()

if __name__ == "__main__":
    main()
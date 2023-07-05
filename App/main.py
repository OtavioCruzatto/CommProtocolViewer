import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

def main():

    # Cria uma aplicacao Qt
    app = QApplication(sys.argv)

    # Instancia um objeto do tipo MainWindow (classe acima)
    window = MainWindow()

    # Exibe a interface grafica
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

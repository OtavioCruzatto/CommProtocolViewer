from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from Gui.ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Slot, Qt
from ProtocoloDeComunicacao.pacote_de_dados import PacoteDeDados


class MainWindow(QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()

        # Carrega a classe python gerada pelo arquivo .ui (convertida para python pelo pyside6-uic
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Codificador e decodificador")

        # Altera o texto do botao e adiciona o sinal do clique do botao ao slot (metodo: exibe_mensagem_no_terminal)
        self.ui.decodificar_QPushButton.clicked.connect(self.decodificar_pacote)

        # Inicializa a tabela de pacotes decodificados
        self.ui.pacotes_decodificados_QTableWidget.setRowCount(1)
        self.ui.pacotes_decodificados_QTableWidget.setColumnCount(6)
        self.ui.pacotes_decodificados_QTableWidget.setHorizontalHeaderLabels(["Inicializador 1", "Inicializador 2", "Comando",
                                                                        "Qtd de dados", "Dados", "CRC8"])

        self.pacotes_validos_decodificados = []
        self.linhas_da_tabela = 1
        self.qtd_max_de_pacotes = 200

        self.pacote_codificado_str = ""
        self.ui.codificar_QPushButton.clicked.connect(self.codificar_pacote)
        self.ui.pacotes_codificados_QTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)


    @Slot()
    def decodificar_pacote(self):
        texto_de_entrada = self.ui.pacote_para_decodificar_QLineEdit.text()
        lista_com_elementos_de_entrada_texto = texto_de_entrada.split(" ")
        pacote = PacoteDeDados()

        try:
            lista_com_elementos_de_entrada_texto = MainWindow.limpar_espacos_vazios_da_entrada(lista_com_elementos_de_entrada_texto)
            lista_com_elementos_de_entrada_int = MainWindow.converter_lista_de_string_para_inteiros(lista_com_elementos_de_entrada_texto)
            pacote_para_decodificar_com_dados = lista_com_elementos_de_entrada_int
            pacote.decodificar(pacote_para_decodificar_com_dados)
            if pacote.esta_valido():
                if len(self.pacotes_validos_decodificados) < self.qtd_max_de_pacotes:
                    self.pacotes_validos_decodificados.append(pacote)
                    self.exibir_dados_decodificados_na_tabela()
                    self.atualiza_quantidade_de_linhas_da_tabela()
                    self.ui.pacotes_decodificados_QTableWidget.scrollToBottom()
                else:
                    print("Quantidade de pacotes limite atingida.")
        except ValueError as err:
            print("Pacote invalido.", end=" ")
            print(err)
            del pacote
        except TypeError as err:
            print("Pacote invalido.", end=" ")
            print(err)
            del pacote


    def exibir_dados_decodificados_na_tabela(self):
        item_inicializador_1 = QTableWidgetItem("0x" + format(self.pacotes_validos_decodificados[-1].get_inicializador_1(), "02X"))
        item_inicializador_1.setTextAlignment(Qt.AlignCenter)

        item_inicializador_2 = QTableWidgetItem("0x" + format(self.pacotes_validos_decodificados[-1].get_inicializador_2(), "02X"))
        item_inicializador_2.setTextAlignment(Qt.AlignCenter)

        item_comando = QTableWidgetItem("0x" + format(self.pacotes_validos_decodificados[-1].get_comando(), "02X"))
        item_comando.setTextAlignment(Qt.AlignCenter)

        item_qtd_dados = QTableWidgetItem(str(self.pacotes_validos_decodificados[-1].get_quantidade_de_dados()))
        item_qtd_dados.setTextAlignment(Qt.AlignCenter)

        dados = ""
        if self.pacotes_validos_decodificados[-1].get_quantidade_de_dados() > 0:
            for dado in self.pacotes_validos_decodificados[-1].get_dados():
                dados += "0x" + format(dado, "02X") + " "
        dados = dados.strip()
        item_dados = QTableWidgetItem(dados)
        item_dados.setTextAlignment(Qt.AlignCenter)

        item_crc8 = QTableWidgetItem("0x" + format(self.pacotes_validos_decodificados[-1].get_crc8(), "02X"))
        item_crc8.setTextAlignment(Qt.AlignCenter)

        self.ui.pacotes_decodificados_QTableWidget.setItem(self.linhas_da_tabela - 1, 0, item_inicializador_1)
        self.ui.pacotes_decodificados_QTableWidget.setItem(self.linhas_da_tabela - 1, 1, item_inicializador_2)
        self.ui.pacotes_decodificados_QTableWidget.setItem(self.linhas_da_tabela - 1, 2, item_comando)
        self.ui.pacotes_decodificados_QTableWidget.setItem(self.linhas_da_tabela - 1, 3, item_qtd_dados)
        self.ui.pacotes_decodificados_QTableWidget.setItem(self.linhas_da_tabela - 1, 4, item_dados)
        self.ui.pacotes_decodificados_QTableWidget.setItem(self.linhas_da_tabela - 1, 5, item_crc8)


    def atualiza_quantidade_de_linhas_da_tabela(self):
        self.ui.pacotes_decodificados_QTableWidget.setRowCount(len(self.pacotes_validos_decodificados) + 1)
        self.linhas_da_tabela += 1


    @staticmethod
    def limpar_espacos_vazios_da_entrada(lista_com_elementos_de_entrada_texto):
        contador_de_itens_vazios = 0

        for item in lista_com_elementos_de_entrada_texto:
            if item == "":
                contador_de_itens_vazios += 1

        for _ in range(contador_de_itens_vazios):
            lista_com_elementos_de_entrada_texto.remove("")

        return lista_com_elementos_de_entrada_texto


    @staticmethod
    def converter_lista_de_string_para_inteiros(lista_com_elementos_de_entrada_texto):
        lista_de_inteiros = []

        try:
            for item in lista_com_elementos_de_entrada_texto:
                lista_de_inteiros.append(int(item, 16))
        except ValueError:
            raise

        return lista_de_inteiros


    @Slot()
    def codificar_pacote(self):
        inicializador_1_str = self.ui.inicializador_1_QLineEdit.text()
        inicializador_2_str = self.ui.inicializador_2_QLineEdit.text()
        comando_str = self.ui.comando_QLineEdit.text()
        dados_str = self.ui.dados_QLineEdit.text()
        dados_str = dados_str.strip()

        lista_de_dados_str = dados_str.split(" ")

        try:
            lista_de_dados_str = MainWindow.limpar_espacos_vazios_da_entrada(lista_de_dados_str)
            lista_de_dados_int = MainWindow.converter_lista_de_string_para_inteiros(lista_de_dados_str)

            inicializador_1_int = int(inicializador_1_str, 16)
            inicializador_2_int = int(inicializador_2_str, 16)
            comando_int = int(comando_str, 16)

            pacote = PacoteDeDados()
            pacote.montar(inicializador_1_int, inicializador_2_int, comando_int, lista_de_dados_int)

            if pacote.esta_valido():
                for byte in pacote.get_pacote():
                    self.pacote_codificado_str += "0x" + format(byte, "02X") + " "
                pacote_str = self.pacote_codificado_str.strip()
                self.pacote_codificado_str += "\n"
                self.ui.pacotes_codificados_QTextEdit.setText(pacote_str)
                self.ui.pacotes_codificados_QTextEdit.verticalScrollBar().setSliderPosition(len(pacote_str))
            else:
                print("Entrada invalida. Os valores informados devem estar no formato hexadecimal. Ex: '0xAA', 'AA', '0XAA'.")

        except ValueError:
            print("Entrada invalida. Os valores informados devem estar no formato hexadecimal. Ex: '0xAA', 'AA', '0XAA'.")

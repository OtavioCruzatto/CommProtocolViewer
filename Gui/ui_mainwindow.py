# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.decodificar_QGroupBox = QGroupBox(self.centralwidget)
        self.decodificar_QGroupBox.setObjectName(u"decodificar_QGroupBox")
        self.decodificar_QGroupBox.setGeometry(QRect(10, 280, 981, 471))
        self.pacote_para_decodificar_QLineEdit = QLineEdit(self.decodificar_QGroupBox)
        self.pacote_para_decodificar_QLineEdit.setObjectName(u"pacote_para_decodificar_QLineEdit")
        self.pacote_para_decodificar_QLineEdit.setGeometry(QRect(10, 40, 801, 41))
        self.decodificar_QPushButton = QPushButton(self.decodificar_QGroupBox)
        self.decodificar_QPushButton.setObjectName(u"decodificar_QPushButton")
        self.decodificar_QPushButton.setGeometry(QRect(820, 40, 151, 41))
        self.pacotes_decodificados_QTableWidget = QTableWidget(self.decodificar_QGroupBox)
        self.pacotes_decodificados_QTableWidget.setObjectName(u"pacotes_decodificados_QTableWidget")
        self.pacotes_decodificados_QTableWidget.setGeometry(QRect(10, 90, 961, 371))
        self.pacote_para_decodificar_QLabel = QLabel(self.decodificar_QGroupBox)
        self.pacote_para_decodificar_QLabel.setObjectName(u"pacote_para_decodificar_QLabel")
        self.pacote_para_decodificar_QLabel.setGeometry(QRect(11, 25, 49, 16))
        self.codificar_QGroupBox = QGroupBox(self.centralwidget)
        self.codificar_QGroupBox.setObjectName(u"codificar_QGroupBox")
        self.codificar_QGroupBox.setGeometry(QRect(10, 10, 981, 251))
        self.codificar_QPushButton = QPushButton(self.codificar_QGroupBox)
        self.codificar_QPushButton.setObjectName(u"codificar_QPushButton")
        self.codificar_QPushButton.setGeometry(QRect(820, 39, 151, 44))
        self.pacotes_codificados_QTextEdit = QTextEdit(self.codificar_QGroupBox)
        self.pacotes_codificados_QTextEdit.setObjectName(u"pacotes_codificados_QTextEdit")
        self.pacotes_codificados_QTextEdit.setGeometry(QRect(10, 90, 961, 151))
        self.inicializador_1_QLineEdit = QLineEdit(self.codificar_QGroupBox)
        self.inicializador_1_QLineEdit.setObjectName(u"inicializador_1_QLineEdit")
        self.inicializador_1_QLineEdit.setGeometry(QRect(10, 40, 101, 41))
        self.inicializador_2_QLineEdit = QLineEdit(self.codificar_QGroupBox)
        self.inicializador_2_QLineEdit.setObjectName(u"inicializador_2_QLineEdit")
        self.inicializador_2_QLineEdit.setGeometry(QRect(130, 40, 101, 41))
        self.comando_QLineEdit = QLineEdit(self.codificar_QGroupBox)
        self.comando_QLineEdit.setObjectName(u"comando_QLineEdit")
        self.comando_QLineEdit.setGeometry(QRect(250, 40, 101, 41))
        self.dados_QLineEdit = QLineEdit(self.codificar_QGroupBox)
        self.dados_QLineEdit.setObjectName(u"dados_QLineEdit")
        self.dados_QLineEdit.setGeometry(QRect(370, 40, 441, 41))
        self.inicializador_1_QLabel = QLabel(self.codificar_QGroupBox)
        self.inicializador_1_QLabel.setObjectName(u"inicializador_1_QLabel")
        self.inicializador_1_QLabel.setGeometry(QRect(11, 25, 81, 16))
        self.inicializador_2_QLabel = QLabel(self.codificar_QGroupBox)
        self.inicializador_2_QLabel.setObjectName(u"inicializador_2_QLabel")
        self.inicializador_2_QLabel.setGeometry(QRect(131, 25, 81, 16))
        self.comando_QLabel = QLabel(self.codificar_QGroupBox)
        self.comando_QLabel.setObjectName(u"comando_QLabel")
        self.comando_QLabel.setGeometry(QRect(251, 25, 61, 16))
        self.dados_QLabel = QLabel(self.codificar_QGroupBox)
        self.dados_QLabel.setObjectName(u"dados_QLabel")
        self.dados_QLabel.setGeometry(QRect(371, 25, 41, 16))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 267, 981, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.decodificar_QGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Decodificar", None))
        self.decodificar_QPushButton.setText(QCoreApplication.translate("MainWindow", u"Decodificar", None))
        self.pacote_para_decodificar_QLabel.setText(QCoreApplication.translate("MainWindow", u"Pacote", None))
        self.codificar_QGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Codificar", None))
        self.codificar_QPushButton.setText(QCoreApplication.translate("MainWindow", u"Codificar", None))
        self.inicializador_1_QLabel.setText(QCoreApplication.translate("MainWindow", u"Inicializador 1", None))
        self.inicializador_2_QLabel.setText(QCoreApplication.translate("MainWindow", u"Inicializador 2", None))
        self.comando_QLabel.setText(QCoreApplication.translate("MainWindow", u"Comando", None))
        self.dados_QLabel.setText(QCoreApplication.translate("MainWindow", u"Dados", None))
    # retranslateUi


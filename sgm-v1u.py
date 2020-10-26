# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\masaüstü\sendgmail-v1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import os
import  sys
from PyQt5 import QtCore, QtGui, QtWidgets








class Ui_MaiWindow(object):
    def setupUi(self, MaiWindow):
        MaiWindow.setObjectName("MaiWindow")
        MaiWindow.resize(747, 396)
        self.centralwidget = QtWidgets.QWidget(MaiWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gonderen_ep = QtWidgets.QTextEdit(self.centralwidget)
        self.gonderen_ep.setGeometry(QtCore.QRect(0, 40, 251, 31))
        self.gonderen_ep.setObjectName("gonderen_ep")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.label.setObjectName("label")
        self.parola = QtWidgets.QTextEdit(self.centralwidget)
        self.parola.setGeometry(QtCore.QRect(0, 100, 251, 31))
        self.parola.setObjectName("parola")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 241, 21))
        self.label_2.setObjectName("label_2")
        self.alici_ep = QtWidgets.QTextEdit(self.centralwidget)
        self.alici_ep.setGeometry(QtCore.QRect(0, 160, 251, 31))
        self.alici_ep.setObjectName("alici_ep")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 135, 241, 21))
        self.label_3.setObjectName("label_3")
        self.gonder = QtWidgets.QPushButton(self.centralwidget)
        self.gonder.setGeometry(QtCore.QRect(30, 220, 93, 28))
        self.gonder.setObjectName("gonder")
        self.metin = QtWidgets.QTextEdit(self.centralwidget)
        self.metin.setGeometry(QtCore.QRect(280, 100, 461, 241))
        self.metin.setObjectName("metin")
        self.konu = QtWidgets.QTextEdit(self.centralwidget)
        self.konu.setGeometry(QtCore.QRect(280, 40, 461, 31))
        self.konu.setObjectName("konu")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 20, 211, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 80, 201, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 241, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 320, 231, 16))
        self.label_7.setObjectName("label_7")
        MaiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MaiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 747, 26))
        self.menubar.setObjectName("menubar")
        self.menu_k = QtWidgets.QMenu(self.menubar)
        self.menu_k.setObjectName("menu_k")
        self.menuKaydet = QtWidgets.QMenu(self.menubar)
        self.menuKaydet.setObjectName("menuKaydet")
        self.menuTemizle = QtWidgets.QMenu(self.menubar)
        self.menuTemizle.setObjectName("menuTemizle")
        MaiWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MaiWindow)
        self.statusbar.setObjectName("statusbar")
        MaiWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuKaydet.menuAction())
        self.menubar.addAction(self.menuTemizle.menuAction())
        self.menubar.addAction(self.menu_k.menuAction())

        self.retranslateUi(MaiWindow)
        QtCore.QMetaObject.connectSlotsByName(MaiWindow)
        MaiWindow.setTabOrder(self.gonderen_ep, self.parola)
        MaiWindow.setTabOrder(self.parola, self.alici_ep)
        MaiWindow.setTabOrder(self.alici_ep, self.gonder)
        MaiWindow.setTabOrder(self.gonder, self.konu)
        MaiWindow.setTabOrder(self.konu, self.metin)

    def retranslateUi(self, MaiWindow):
        _translate = QtCore.QCoreApplication.translate
        MaiWindow.setWindowTitle(_translate("MaiWindow", "SendGMail"))
        self.label.setText(_translate("MaiWindow", "Gönderen Eposta"))
        self.label_2.setText(_translate("MaiWindow", "Parola"))
        self.label_3.setText(_translate("MaiWindow", "Alıcı"))
        self.gonder.setText(_translate("MaiWindow", "Gönder"))
        self.label_4.setText(_translate("MaiWindow", "Konu"))
        self.label_5.setText(_translate("MaiWindow", "Metin"))
        self.pushButton.setText(_translate("MaiWindow", "Çık"))
        self.label_6.setText(_translate("MaiWindow", "GMail ile mail göndermek için geliştirildi."))
        self.label_7.setText(_translate("MaiWindow", "                               ouz-dev 2020  v1"))
        self.menu_k.setTitle(_translate("MaiWindow", "Çıkış"))
        self.menuKaydet.setTitle(_translate("MaiWindow", "Kaydet"))
        self.menuTemizle.setTitle(_translate("MaiWindow", "Temizle"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MaiWindow = QtWidgets.QMainWindow()
    ui = Ui_MaiWindow()
    ui.setupUi(MaiWindow)
    MaiWindow.show()
    sys.exit(app.exec_())

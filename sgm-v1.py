# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\masaüstü\sendgmail-v1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import os
import  sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp,QAction




class Ui_MaiWindow(object):
    def setupUi(self, MaiWindow):
        MaiWindow.setObjectName("MaiWindow")
        MaiWindow.resize(747, 396)
        super().__init__()
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

        self.gonder.clicked.connect(self.mail_send)
        self.pushButton.clicked.connect(self.cikis)
        #self.menuTemizle.triggered(self.temizle)
        self.menu_k.triggered.connect(self.cikis)





    def retranslateUi(self, MaiWindow):
        _translate = QtCore.QCoreApplication.translate
        MaiWindow.setWindowTitle(_translate("MaiWindow", "SendGMail"))
        self.label.setText(_translate("MaiWindow", "From"))
        self.label_2.setText(_translate("MaiWindow", "Mail Password"))
        self.label_3.setText(_translate("MaiWindow", "To"))
        self.gonder.setText(_translate("MaiWindow", "Send"))
        self.label_4.setText(_translate("MaiWindow", "Title"))
        self.label_5.setText(_translate("MaiWindow", "Body"))
        self.pushButton.setText(_translate("MaiWindow", "Exit"))
        self.label_6.setText(_translate("MaiWindow", "Created for send Gmail"))
        self.label_7.setText(_translate("MaiWindow", "                               ouz-dev 2020  v1"))
        self.menu_k.setTitle(_translate("MaiWindow", "Exit"))
        self.menuKaydet.setTitle(_translate("MaiWindow", "Save"))
        self.menuTemizle.setTitle(_translate("MaiWindow", "Clear"))

    def temizle(self):
        self.gonderen_ep.clear()
        self.parola.clear()
        self.alici_ep.clear()
        self.konu.clear()
        self.metin.clear()



    def mail_send(self):
        mesaj=MIMEMultipart()
        mesaj["From"]=self.gonderen_ep.toPlainText()
        mesaj["To"]=self.alici_ep.toPlainText()
        mesaj["Subject"]=self.konu.toPlainText()
        yazi=self.metin.toPlainText()
        mesaj_govde=MIMEText(yazi,"plain")
        mesaj.attach(mesaj_govde)
        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(self.gonderen_ep.toPlainText(), self.parola.toPlainText())
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("successfull.....")
            mail.close()
        except:
            sys.stderr.write("error....")
            sys.stderr.flush()



    def cikis(self):
        qApp.quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MaiWindow = QtWidgets.QMainWindow()
    ui = Ui_MaiWindow()
    ui.setupUi(MaiWindow)
    MaiWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import asyncio
import discord
from discord import Webhook
import aiohttp
import json
from functools import partial
import ctypes

__version__ = "2.1"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(851, 441)
        MainWindow.setFixedSize(851, 441)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.statusBar = QtWidgets.QLabel(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(10, 411, 211, 30))
        self.statusBar.setObjectName("statusBar")
        self.pos1 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos1.setGeometry(QtCore.QRect(60, 80, 141, 20))
        self.pos1.setObjectName("pos1")
        self.pos2 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos2.setGeometry(QtCore.QRect(60, 110, 141, 20))
        self.pos2.setObjectName("pos2")
        self.pos3 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos3.setGeometry(QtCore.QRect(60, 140, 141, 20))
        self.pos3.setObjectName("pos3")
        self.pos4 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos4.setGeometry(QtCore.QRect(60, 170, 141, 20))
        self.pos4.setObjectName("pos4")
        self.pos5 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos5.setGeometry(QtCore.QRect(60, 200, 141, 20))
        self.pos5.setObjectName("pos5")
        self.pos6 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos6.setGeometry(QtCore.QRect(60, 250, 141, 20))
        self.pos6.setObjectName("pos6")
        self.pos7 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos7.setGeometry(QtCore.QRect(60, 280, 141, 20))
        self.pos7.setObjectName("pos7")
        self.pos8 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos8.setGeometry(QtCore.QRect(60, 310, 141, 20))
        self.pos8.setObjectName("pos8")
        self.pos9 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos9.setGeometry(QtCore.QRect(60, 340, 141, 20))
        self.pos9.setObjectName("pos9")
        self.pos10 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos10.setGeometry(QtCore.QRect(60, 370, 141, 20))
        self.pos10.setObjectName("pos10")
        self.posPointsButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton1.setGeometry(QtCore.QRect(220, 80, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.posPointsButton1.setFont(font)
        self.posPointsButton1.setObjectName("posPointsButton1")
        self.posPointsButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton2.setGeometry(QtCore.QRect(220, 110, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton2.setFont(font)
        self.posPointsButton2.setObjectName("posPointsButton2")
        self.posPointsButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton3.setGeometry(QtCore.QRect(220, 140, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton3.setFont(font)
        self.posPointsButton3.setObjectName("posPointsButton3")
        self.posPointsButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton4.setGeometry(QtCore.QRect(220, 170, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton4.setFont(font)
        self.posPointsButton4.setObjectName("posPointsButton4")
        self.posPointsButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton5.setGeometry(QtCore.QRect(220, 200, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton5.setFont(font)
        self.posPointsButton5.setObjectName("posPointsButton5")
        self.posPointsButton9 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton9.setGeometry(QtCore.QRect(220, 340, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton9.setFont(font)
        self.posPointsButton9.setObjectName("posPointsButton9")
        self.posPointsButton10 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton10.setGeometry(QtCore.QRect(220, 370, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton10.setFont(font)
        self.posPointsButton10.setObjectName("posPointsButton10")
        self.posPointsButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton7.setGeometry(QtCore.QRect(220, 280, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton7.setFont(font)
        self.posPointsButton7.setObjectName("posPointsButton7")
        self.posPointsButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton6.setGeometry(QtCore.QRect(220, 250, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton6.setFont(font)
        self.posPointsButton6.setObjectName("posPointsButton6")
        self.posPointsButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton8.setGeometry(QtCore.QRect(220, 310, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton8.setFont(font)
        self.posPointsButton8.setObjectName("posPointsButton8")
        self.posAdd1 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd1.setGeometry(QtCore.QRect(270, 80, 51, 23))
        self.posAdd1.setObjectName("posAdd1")
        self.posRemove1 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove1.setGeometry(QtCore.QRect(330, 80, 51, 23))
        self.posRemove1.setObjectName("posRemove1")
        self.posAdd2 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd2.setGeometry(QtCore.QRect(270, 110, 51, 23))
        self.posAdd2.setObjectName("posAdd2")
        self.posAdd3 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd3.setGeometry(QtCore.QRect(270, 140, 51, 23))
        self.posAdd3.setObjectName("posAdd3")
        self.posAdd4 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd4.setGeometry(QtCore.QRect(270, 170, 51, 23))
        self.posAdd4.setObjectName("posAdd4")
        self.posAdd5 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd5.setGeometry(QtCore.QRect(270, 200, 51, 23))
        self.posAdd5.setObjectName("posAdd5")
        self.posRemove2 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove2.setGeometry(QtCore.QRect(330, 110, 51, 23))
        self.posRemove2.setObjectName("posRemove2")
        self.posRemove3 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove3.setGeometry(QtCore.QRect(330, 140, 51, 23))
        self.posRemove3.setObjectName("posRemove3")
        self.posRemove4 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove4.setGeometry(QtCore.QRect(330, 170, 51, 23))
        self.posRemove4.setObjectName("posRemove4")
        self.posRemove5 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove5.setGeometry(QtCore.QRect(330, 200, 51, 23))
        self.posRemove5.setObjectName("posRemove5")
        self.posAdd6 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd6.setGeometry(QtCore.QRect(270, 250, 51, 23))
        self.posAdd6.setObjectName("posAdd6")
        self.posAdd7 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd7.setGeometry(QtCore.QRect(270, 280, 51, 23))
        self.posAdd7.setObjectName("posAdd7")
        self.posAdd8 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd8.setGeometry(QtCore.QRect(270, 310, 51, 23))
        self.posAdd8.setObjectName("posAdd8")
        self.posAdd9 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd9.setGeometry(QtCore.QRect(270, 340, 51, 23))
        self.posAdd9.setObjectName("posAdd9")
        self.posAdd10 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd10.setGeometry(QtCore.QRect(270, 370, 51, 23))
        self.posAdd10.setObjectName("posAdd10")
        self.posRemove10 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove10.setGeometry(QtCore.QRect(330, 370, 51, 23))
        self.posRemove10.setObjectName("posRemove10")
        self.posRemove7 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove7.setGeometry(QtCore.QRect(330, 280, 51, 23))
        self.posRemove7.setObjectName("posRemove7")
        self.posRemove9 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove9.setGeometry(QtCore.QRect(330, 340, 51, 23))
        self.posRemove9.setObjectName("posRemove9")
        self.posRemove8 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove8.setGeometry(QtCore.QRect(330, 310, 51, 23))
        self.posRemove8.setObjectName("posRemove8")
        self.posRemove6 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove6.setGeometry(QtCore.QRect(330, 250, 51, 23))
        self.posRemove6.setObjectName("posRemove6")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(240, 10, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setObjectName("title")
        self.syncButton = QtWidgets.QPushButton(self.centralwidget)
        self.syncButton.setGeometry(QtCore.QRect(770, 410, 75, 23))
        self.syncButton.setObjectName("syncButton")
        self.points1_5 = QtWidgets.QLabel(self.centralwidget)
        self.points1_5.setEnabled(False)
        self.points1_5.setGeometry(QtCore.QRect(220, 60, 41, 21))
        self.points1_5.setObjectName("points1_5")
        self.num1_5 = QtWidgets.QLabel(self.centralwidget)
        self.num1_5.setGeometry(QtCore.QRect(40, 80, 20, 141))
        self.num1_5.setObjectName("num1_5")
        self.num6_10 = QtWidgets.QLabel(self.centralwidget)
        self.num6_10.setGeometry(QtCore.QRect(35, 250, 21, 141))
        self.num6_10.setObjectName("num6_10")
        self.posRemove18 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove18.setGeometry(QtCore.QRect(760, 310, 51, 23))
        self.posRemove18.setObjectName("posRemove18")
        self.posRemove19 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove19.setGeometry(QtCore.QRect(760, 340, 51, 23))
        self.posRemove19.setObjectName("posRemove19")
        self.posAdd18 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd18.setGeometry(QtCore.QRect(700, 310, 51, 23))
        self.posAdd18.setObjectName("posAdd18")
        self.pos17 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos17.setGeometry(QtCore.QRect(490, 280, 141, 20))
        self.pos17.setObjectName("pos17")
        self.pos19 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos19.setGeometry(QtCore.QRect(490, 340, 141, 20))
        self.pos19.setObjectName("pos19")
        self.posPointsButton17 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton17.setGeometry(QtCore.QRect(650, 280, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton17.setFont(font)
        self.posPointsButton17.setObjectName("posPointsButton17")
        self.num16_20 = QtWidgets.QLabel(self.centralwidget)
        self.num16_20.setGeometry(QtCore.QRect(464, 250, 21, 141))
        self.num16_20.setObjectName("num16_20")
        self.posAdd17 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd17.setGeometry(QtCore.QRect(700, 280, 51, 23))
        self.posAdd17.setObjectName("posAdd17")
        self.posPointsButton18 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton18.setGeometry(QtCore.QRect(650, 310, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton18.setFont(font)
        self.posPointsButton18.setObjectName("posPointsButton18")
        self.posRemove17 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove17.setGeometry(QtCore.QRect(760, 280, 51, 23))
        self.posRemove17.setObjectName("posRemove17")
        self.posAdd20 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd20.setGeometry(QtCore.QRect(700, 370, 51, 23))
        self.posAdd20.setObjectName("posAdd20")
        self.pos18 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos18.setGeometry(QtCore.QRect(490, 310, 141, 20))
        self.pos18.setObjectName("pos18")
        self.posPointsButton19 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton19.setGeometry(QtCore.QRect(650, 340, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton19.setFont(font)
        self.posPointsButton19.setObjectName("posPointsButton19")
        self.pos20 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos20.setGeometry(QtCore.QRect(490, 370, 141, 20))
        self.pos20.setObjectName("pos20")
        self.posPointsButton20 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton20.setGeometry(QtCore.QRect(650, 370, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton20.setFont(font)
        self.posPointsButton20.setObjectName("posPointsButton20")
        self.posAdd19 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd19.setGeometry(QtCore.QRect(700, 340, 51, 23))
        self.posAdd19.setObjectName("posAdd19")
        self.posRemove16 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove16.setGeometry(QtCore.QRect(760, 250, 51, 23))
        self.posRemove16.setObjectName("posRemove16")
        self.posRemove20 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove20.setGeometry(QtCore.QRect(760, 370, 51, 23))
        self.posRemove20.setObjectName("posRemove20")
        self.posAdd16 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd16.setGeometry(QtCore.QRect(700, 250, 51, 23))
        self.posAdd16.setObjectName("posAdd16")
        self.posPointsButton16 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton16.setGeometry(QtCore.QRect(650, 250, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton16.setFont(font)
        self.posPointsButton16.setObjectName("posPointsButton16")
        self.pos16 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos16.setGeometry(QtCore.QRect(490, 250, 141, 20))
        self.pos16.setObjectName("pos16")
        self.points11_15 = QtWidgets.QLabel(self.centralwidget)
        self.points11_15.setEnabled(False)
        self.points11_15.setGeometry(QtCore.QRect(650, 60, 41, 21))
        self.points11_15.setObjectName("points11_15")
        self.posPointsButton14 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton14.setGeometry(QtCore.QRect(650, 170, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton14.setFont(font)
        self.posPointsButton14.setObjectName("posPointsButton14")
        self.posAdd12 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd12.setGeometry(QtCore.QRect(700, 110, 51, 23))
        self.posAdd12.setObjectName("posAdd12")
        self.pos13 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos13.setGeometry(QtCore.QRect(490, 140, 141, 20))
        self.pos13.setObjectName("pos13")
        self.posPointsButton15 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton15.setGeometry(QtCore.QRect(650, 200, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton15.setFont(font)
        self.posPointsButton15.setObjectName("posPointsButton15")
        self.posAdd15 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd15.setGeometry(QtCore.QRect(700, 200, 51, 23))
        self.posAdd15.setObjectName("posAdd15")
        self.posPointsButton12 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton12.setGeometry(QtCore.QRect(650, 110, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton12.setFont(font)
        self.posPointsButton12.setObjectName("posPointsButton12")
        self.posRemove12 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove12.setGeometry(QtCore.QRect(760, 110, 51, 23))
        self.posRemove12.setObjectName("posRemove12")
        self.posAdd13 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd13.setGeometry(QtCore.QRect(700, 140, 51, 23))
        self.posAdd13.setObjectName("posAdd13")
        self.posRemove11 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove11.setGeometry(QtCore.QRect(760, 80, 51, 23))
        self.posRemove11.setObjectName("posRemove11")
        self.num11_15 = QtWidgets.QLabel(self.centralwidget)
        self.num11_15.setGeometry(QtCore.QRect(464, 80, 20, 141))
        self.num11_15.setObjectName("num11_15")
        self.posRemove13 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove13.setGeometry(QtCore.QRect(760, 140, 51, 23))
        self.posRemove13.setObjectName("posRemove13")
        self.posAdd11 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd11.setGeometry(QtCore.QRect(700, 80, 51, 23))
        self.posAdd11.setObjectName("posAdd11")
        self.pos11 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos11.setGeometry(QtCore.QRect(490, 80, 141, 20))
        self.pos11.setObjectName("pos11")
        self.posRemove15 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove15.setGeometry(QtCore.QRect(760, 200, 51, 23))
        self.posRemove15.setObjectName("posRemove15")
        self.pos15 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos15.setGeometry(QtCore.QRect(490, 200, 141, 20))
        self.pos15.setObjectName("pos15")
        self.pos12 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos12.setGeometry(QtCore.QRect(490, 110, 141, 20))
        self.pos12.setObjectName("pos12")
        self.posPointsButton13 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton13.setGeometry(QtCore.QRect(650, 140, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.posPointsButton13.setFont(font)
        self.posPointsButton13.setObjectName("posPointsButton13")
        self.pos14 = QtWidgets.QLineEdit(self.centralwidget)
        self.pos14.setGeometry(QtCore.QRect(490, 170, 141, 20))
        self.pos14.setObjectName("pos14")
        self.posPointsButton11 = QtWidgets.QPushButton(self.centralwidget)
        self.posPointsButton11.setGeometry(QtCore.QRect(650, 80, 41, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.posPointsButton11.setFont(font)
        self.posPointsButton11.setObjectName("posPointsButton11")
        self.posRemove14 = QtWidgets.QPushButton(self.centralwidget)
        self.posRemove14.setGeometry(QtCore.QRect(760, 170, 51, 23))
        self.posRemove14.setObjectName("posRemove14")
        self.posAdd14 = QtWidgets.QPushButton(self.centralwidget)
        self.posAdd14.setGeometry(QtCore.QRect(700, 170, 51, 23))
        self.posAdd14.setObjectName("posAdd14")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.statusBar.setText(_translate("MainWindow", "Status: Loaded from file"))


        # Player Names
        for index in range(19):
            try:
                playerName = sorted_players[index]
            except IndexError:
                playerName = ""
            pos = getattr(self, f"pos{index + 1}")
            pos.setText(_translate("MainWindow", playerName))

        # self.pos1.setText(_translate("MainWindow", sorted_players[0]))
        # ...
        # self.pos20.setText(_translate("MainWindow", sorted_players[19]))


        # Point Counters
        for index in range(20):
            try:
                points = str(sorted_points[index])
            except IndexError:
                points = ""
            posPointsButton = getattr(self, f"posPointsButton{index + 1}")
            posPointsButton.setText(_translate("MainWindow", points))

        # self.posPointsButton1.setText(_translate("MainWindow", str(sorted_points[0])))
        # ...
        # self.posPointsButton20.setText(_translate("MainWindow", str(sorted_points[19])))

        # Add/Remove Buttons + Click Functionality
        for index in range(20):
            posAdd = getattr(self, f"posAdd{index + 1}")
            posRemove = getattr(self, f"posRemove{index + 1}")

            posAdd.setText(_translate("MainWindow", "Add"))
            posRemove.setText(_translate("MainWindow", "Remove"))
            posAdd.clicked.connect(partial(self.addPlace, index + 1))
            posRemove.clicked.connect(partial(self.removePlace, index + 1))

        # Other
        self.title.setText(_translate("MainWindow", "Jama Zonies PR Leaderboard"))
        self.syncButton.setText(_translate("MainWindow", "Sync Now"))

        self.num1_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">1.</span></p><p><span style=\" font-size:9pt;\">2.</span></p><p><span style=\" font-size:9pt;\">3.</span></p><p><span style=\" font-size:9pt;\">4.</span></p><p><span style=\" font-size:9pt;\">5.</span></p></body></html>"))
        self.num6_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">6.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">7.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">8.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">9.</span></p><p align=\"center\"><span style=\" font-size:9pt;\">10.</span></p></body></html>"))
        self.num11_15.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:9pt;\">11.</span></p><p><span style=\" font-size:9pt;\">12.</span></p><p><span style=\" font-size:9pt;\">13.</span></p><p><span style=\" font-size:9pt;\">14.</span></p><p><span style=\" font-size:9pt;\">15.</span></p></body></html>"))
        self.num16_20.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:9pt;\">16.</span></p><p><span style=\" font-size:9pt;\">17.</span></p><p><span style=\" font-size:9pt;\">18.</span></p><p><span style=\" font-size:9pt;\">19.</span></p><p><span style=\" font-size:9pt;\">20.</span></p></body></html>"))

        self.points1_5.setText(_translate("MainWindow", "  Points"))
        self.points11_15.setText(_translate("MainWindow", "  Points"))

        self.syncButton.clicked.connect(self.initSync)

        global changes_saved_on_first_status_fuck_you
        changes_saved_on_first_status_fuck_you = True

        # Add
        # self.posAdd1.setText(_translate("MainWindow", "Add"))
        # ...
        # self.posAdd20.setText(_translate("MainWindow", "Add"))


        # Remove
        # self.posRemove1.setText(_translate("MainWindow", "Remove"))
        # ...
        # self.posRemove20.setText(_translate("MainWindow", "Remove"))

        # man i could write a function for this
        # Edit: i did ;)

        # Button Logic
        # self.posAdd1.clicked.connect(partial(self.addPlace,1))
        # ...
        # self.posAdd20.clicked.connect(partial(self.addPlace,20))

        # self.posRemove1.clicked.connect(partial(self.removePlace,1))
        # ...
        # self.posRemove20.clicked.connect(partial(self.removePlace,20))


    def addPlace(self, index):
        button = getattr(self, f"posPointsButton{index}")
        try:    # Try updating point values in the sorted_points list, if there is an empty player (no data) then just update point counter directly
            sorted_points[index - 1] += 1
            button.setText(str(sorted_points[index - 1]))
        except IndexError:
            points: str = button.text()
            if points == "":
                points = "0"    # quotes because the below we use int()
            button.setText(str(int(points) + 1))
        if changes_saved_on_first_status_fuck_you:
            self.statusBar.setText("Status: Not saved")

    def removePlace(self, index):
        button = getattr(self, f"posPointsButton{index}")
        try:    # Try updating point values in the sorted_points list, if there is an empty player (no data) then just update point counter directly
            sorted_points[index - 1] -= 1
            button.setText(str(sorted_points[index - 1]))
        except IndexError:
            points: str = button.text()
            if points == "":
                points = "0"  # quotes because the below we use int()
            button.setText(str(int(points) - 1))
        if changes_saved_on_first_status_fuck_you:
            self.statusBar.setText("Status: Not saved")

    # I am too lazy to fix the redundancy here, we don't even use the lists except for startup so why update them and run checks n shit???


    def initSync(self):
        leaderboard_data_from_program_not_file = {self.pos1.text(): self.posPointsButton1.text(),
                                                  self.pos2.text(): self.posPointsButton2.text(),
                                                  self.pos3.text(): self.posPointsButton3.text(),
                                                  self.pos4.text(): self.posPointsButton4.text(),
                                                  self.pos5.text(): self.posPointsButton5.text(),
                                                  self.pos6.text(): self.posPointsButton6.text(),
                                                  self.pos7.text(): self.posPointsButton7.text(),
                                                  self.pos8.text(): self.posPointsButton8.text(),
                                                  self.pos9.text(): self.posPointsButton9.text(),
                                                  self.pos10.text(): self.posPointsButton10.text(),
                                                  self.pos11.text(): self.posPointsButton11.text(),
                                                  self.pos12.text(): self.posPointsButton12.text(),
                                                  self.pos13.text(): self.posPointsButton13.text(),
                                                  self.pos14.text(): self.posPointsButton14.text(),
                                                  self.pos15.text(): self.posPointsButton15.text(),
                                                  self.pos16.text(): self.posPointsButton16.text(),
                                                  self.pos17.text(): self.posPointsButton17.text(),
                                                  self.pos18.text(): self.posPointsButton18.text(),
                                                  self.pos19.text(): self.posPointsButton19.text(),
                                                  self.pos20.text(): self.posPointsButton20.text()
                                                  }
        for playerName in list(leaderboard_data_from_program_not_file.keys()):
            if playerName == "":
                del(leaderboard_data_from_program_not_file[playerName])

        with open("leaderboard_data.json", "w") as local_save:
            json.dump(leaderboard_data_from_program_not_file, local_save, indent=2)

        sendWebhook()

        self.statusBar.setText(f"Status: Saved")

        changes_saved_on_first_status_fuck_you = True


def sendWebhook():
    global sorted_players2
    global sorted_points2
    with open("leaderboard_data.json", "r") as local_save:  # load leaderboard data from file
        for_sending = [json.load(local_save)]

    # leaderboard_data_ints_are_strs = {"player1": 10, "player2": 9, "player3": 8, "player4": 7, "player5": 6, "player6": 5, "player7": 4, "player8": 3, "player9": 2, "player10": 1}

    for_sending2 = [{k: int(v) for k, v in d.items()} for d in
                    map(lambda x: dict(x), for_sending)]
    for_sending3 = dict(
        (key, d[key]) for d in for_sending2 for key in d)
    sorted_players2 = sorted(for_sending3, key=for_sending3.get,
                             reverse=True)  # sort each player (key) by its point value, reversed so highest comes first. a string with only player names is spit out.
    sorted_points2 = []
    for player2 in sorted_players2:  # use the sorted player names to grab their points and file them into a string. a string with only numbers is spit out.
        sorted_points2.append(for_sending3[player2])
    loop = asyncio.new_event_loop()
    loop.run_until_complete(anything(webhook_url))
    loop.close()


async def anything(webhook_url):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(webhook_url, session=session)
        embed = discord.Embed(title="Top 10 PR Standings")

        embed.set_author(name="Jama Zonies PR Leaderboard")


        for index, (sorted_player, sorted_points) in enumerate(zip(sorted_players2, sorted_points2), start=1):
            if index == 1: place = ":first_place:"
            elif index == 2: place = ":second_place:"
            elif index == 3: place = ":third_place:"
            else: place = f"{index}."
            embed.add_field(name=f"{place} {sorted_player} - {sorted_points} points",
                            value="",
                            inline=False)

        # embed.add_field(name=f":first_place: {sorted_players2[0]} - {sorted_points2[0]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f":second_place: {sorted_players2[1]} - {sorted_points2[1]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f":third_place: {sorted_players2[2]} - {sorted_points2[2]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f"4. {sorted_players2[3]} - {sorted_points2[3]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f"5. {sorted_players2[4]} - {sorted_points2[4]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f"6. {sorted_players2[5]} - {sorted_points2[5]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f"7. {sorted_players2[6]} - {sorted_points2[6]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f"8. {sorted_players2[7]} - {sorted_points2[7]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f"9. {sorted_players2[8]} - {sorted_points2[8]} points",
        #                 value="",
        #                 inline=False)
        # embed.add_field(name=f"10. {sorted_players2[9]} - {sorted_points2[9]} points",
        #                 value="",
        #                 inline=False)
        embed.set_footer(text="Version 2.1 | Made by Smelvin")

        await webhook.edit_message(message_id, embed=embed
                                   # , username=""
                                   )


if __name__ == "__main__":
    import sys

    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
            webhook_url = config["webhook_url"]
            message_id = config["message_id"]
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(
            0,
            "Config file not found. Run setup.py",
            "Config Error",
            0x30
        )
        sys.exit(1)

    with open("leaderboard_data.json", "r") as local_save:  # load leaderboard data from file
        leaderboard_data_ints_are_strs = [json.load(local_save)]

    #leaderboard_data_ints_are_strs = [
    #    {"BEATLE": "10", "ADOLLA": "8", "RO2TR": "6", "VISUALS": "4", "DEV": "3", "VORTEX": "3", "STYX": "3", "||": "0",
    #     "||​": "0", "||​​": "0"}]

    leaderboard_data_with_ints_instead_of_strs_FUCK_as_a_str = [{k: int(v) for k, v in d.items()} for d in
                                                                map(lambda x: dict(x), leaderboard_data_ints_are_strs)]
    leaderboard_data = dict(
        (key, d[key]) for d in leaderboard_data_with_ints_instead_of_strs_FUCK_as_a_str for key in d)


    sorted_players = sorted(leaderboard_data, key=leaderboard_data.get,
                            reverse=True)  # sort each player (key) by its point value, reversed so highest comes first. a string with only player names is spit out.

    sorted_points = []
    for player in sorted_players:  # use the sorted player names to grab their points and file them into a string. a string with only numbers is spit out.
        sorted_points.append(leaderboard_data[player])


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

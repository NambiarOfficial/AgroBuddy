# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(130, 10, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setScaledContents(False)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.air_quality_button = QtWidgets.QPushButton(self.centralwidget)
        self.air_quality_button.setGeometry(QtCore.QRect(20, 110, 121, 31))
        self.air_quality_button.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("background/air-quality.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.air_quality_button.setIcon(icon)
        self.air_quality_button.setIconSize(QtCore.QSize(20, 20))
        self.air_quality_button.setShortcut("")
        self.air_quality_button.setCheckable(False)
        self.air_quality_button.setDefault(False)
        self.air_quality_button.setFlat(False)
        self.air_quality_button.setObjectName("air_quality_button")
        self.weather_button = QtWidgets.QPushButton(self.centralwidget)
        self.weather_button.setGeometry(QtCore.QRect(160, 110, 121, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("background/weather.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weather_button.setIcon(icon1)
        self.weather_button.setIconSize(QtCore.QSize(25, 25))
        self.weather_button.setObjectName("weather_button")
        self.crop_selection_button = QtWidgets.QPushButton(self.centralwidget)
        self.crop_selection_button.setGeometry(QtCore.QRect(440, 110, 121, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("background/crop-select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.crop_selection_button.setIcon(icon2)
        self.crop_selection_button.setObjectName("crop_selection_button")
        self.plant_health_button = QtWidgets.QPushButton(self.centralwidget)
        self.plant_health_button.setGeometry(QtCore.QRect(370, 150, 121, 31))
        self.plant_health_button.setObjectName("plant_health_button")
        self.news_button = QtWidgets.QPushButton(self.centralwidget)
        self.news_button.setGeometry(QtCore.QRect(300, 110, 121, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("background/news.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.news_button.setIcon(icon3)
        self.news_button.setIconSize(QtCore.QSize(40, 40))
        self.news_button.setObjectName("news_button")
        self.assistance_button = QtWidgets.QPushButton(self.centralwidget)
        self.assistance_button.setGeometry(QtCore.QRect(90, 150, 121, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("background/assistance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assistance_button.setIcon(icon4)
        self.assistance_button.setObjectName("assistance_button")
        self.forum_button = QtWidgets.QPushButton(self.centralwidget)
        self.forum_button.setGeometry(QtCore.QRect(230, 150, 121, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("background/forum.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forum_button.setIcon(icon5)
        self.forum_button.setIconSize(QtCore.QSize(20, 20))
        self.forum_button.setObjectName("forum_button")
        self.air_quality_label_temp = QtWidgets.QLabel(self.centralwidget)
        self.air_quality_label_temp.setEnabled(True)
        self.air_quality_label_temp.setGeometry(QtCore.QRect(20, 220, 161, 17))
        self.air_quality_label_temp.setObjectName("air_quality_label_temp")
        self.air_quality_label_humidity = QtWidgets.QLabel(self.centralwidget)
        self.air_quality_label_humidity.setEnabled(True)
        self.air_quality_label_humidity.setGeometry(QtCore.QRect(20, 250, 161, 17))
        self.air_quality_label_humidity.setObjectName("air_quality_label_humidity")
        self.air_quality_label_pressure = QtWidgets.QLabel(self.centralwidget)
        self.air_quality_label_pressure.setEnabled(True)
        self.air_quality_label_pressure.setGeometry(QtCore.QRect(20, 280, 161, 17))
        self.air_quality_label_pressure.setObjectName("air_quality_label_pressure")
        self.weather_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.weather_label_1.setGeometry(QtCore.QRect(20, 220, 151, 17))
        self.weather_label_1.setObjectName("weather_label_1")
        self.weather_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.weather_label_2.setGeometry(QtCore.QRect(20, 250, 151, 17))
        self.weather_label_2.setObjectName("weather_label_2")
        self.weather_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.weather_label_3.setGeometry(QtCore.QRect(20, 280, 151, 17))
        self.weather_label_3.setObjectName("weather_label_3")
        self.air_quality_label_methane = QtWidgets.QLabel(self.centralwidget)
        self.air_quality_label_methane.setEnabled(True)
        self.air_quality_label_methane.setGeometry(QtCore.QRect(20, 310, 161, 17))
        self.air_quality_label_methane.setObjectName("air_quality_label_methane")
        self.air_quality_label_nitrogen = QtWidgets.QLabel(self.centralwidget)
        self.air_quality_label_nitrogen.setEnabled(True)
        self.air_quality_label_nitrogen.setGeometry(QtCore.QRect(270, 220, 161, 17))
        self.air_quality_label_nitrogen.setObjectName("air_quality_label_nitrogen")
        self.air_quality_label_carbon_dioxide = QtWidgets.QLabel(self.centralwidget)
        self.air_quality_label_carbon_dioxide.setEnabled(True)
        self.air_quality_label_carbon_dioxide.setGeometry(QtCore.QRect(270, 250, 161, 17))
        self.air_quality_label_carbon_dioxide.setObjectName("air_quality_label_carbon_dioxide")
        self.air_quality_label_oxygen = QtWidgets.QLabel(self.centralwidget)
        self.air_quality_label_oxygen.setEnabled(True)
        self.air_quality_label_oxygen.setGeometry(QtCore.QRect(270, 280, 161, 17))
        self.air_quality_label_oxygen.setObjectName("air_quality_label_oxygen")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "AGROBUDDY"))
        self.air_quality_button.setText(_translate("MainWindow", "Air Quality"))
        self.weather_button.setText(_translate("MainWindow", "Weather"))
        self.crop_selection_button.setText(_translate("MainWindow", "Crop Select"))
        self.plant_health_button.setText(_translate("MainWindow", "Plant Health"))
        self.news_button.setText(_translate("MainWindow", "News"))
        self.assistance_button.setText(_translate("MainWindow", "Assistance"))
        self.forum_button.setText(_translate("MainWindow", "Forum"))
        self.air_quality_label_temp.setText(_translate("MainWindow", "Gas Content 1"))
        self.air_quality_label_humidity.setText(_translate("MainWindow", "Gas Content 2"))
        self.air_quality_label_pressure.setText(_translate("MainWindow", "Gas Content 3"))
        self.weather_label_1.setText(_translate("MainWindow", "Weather Label 1"))
        self.weather_label_2.setText(_translate("MainWindow", "Weather Label 2"))
        self.weather_label_3.setText(_translate("MainWindow", "Weather Label 3"))
        self.air_quality_label_methane.setText(_translate("MainWindow", "Gas Content 3"))
        self.air_quality_label_nitrogen.setText(_translate("MainWindow", "Gas Content 2"))
        self.air_quality_label_carbon_dioxide.setText(_translate("MainWindow", "Gas Content 3"))
        self.air_quality_label_oxygen.setText(_translate("MainWindow", "Gas Content 3"))


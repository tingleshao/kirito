# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

checked = 2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 708)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 608, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("kgui/AquetiLogo.jpg"))
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 500, 531, 41))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setValue(45)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 570, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton2.setGeometry(QtCore.QRect(200, 570, 113, 32))
        self.pushButton2.setObjectName("previewButton")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(60, 480, 621, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(60, 540, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(570, 550, 60, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1315, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.loadModelCheckBox = QtWidgets.QCheckBox(MainWindow)
        self.loadModelCheckBox.setGeometry(350, 598, 20, 20)
        self.loadModelCheckBox.setObjectName("loadModelCheckBox")
        self.loadModelCheckBox.setCheckState(checked)
        self.grabFrameCheckBox = QtWidgets.QCheckBox(MainWindow)
        self.grabFrameCheckBox.setGeometry(350, 630, 20, 20)
        self.grabFrameCheckBox.setObjectName("grabFrameCheckBox")
        self.grabFrameCheckBox.setCheckState(checked)
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(380, 598, 200, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(380, 630, 200, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(350, 662, 20, 20)
        self.label_7.setObjectName("label_7")
        self.ipLabel = QtWidgets.QLineEdit(MainWindow)
        self.ipLabel.setGeometry(QtCore.QRect(380, 662, 200, 16))
        self.ipLabel.setObjectName("ipLabel")
        self.ipLabel.setText("10.0.0.187")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Stitching"))
        self.pushButton2.setText(_translate("MainWindow", "Preview"))
        self.label_2.setText(_translate("MainWindow", "Control points matching threshold (higher value: more features are expected to be found)"))
        self.label_3.setText(_translate("MainWindow", "0.1"))
        self.label_4.setText(_translate("MainWindow", "0.9"))
        self.label_5.setText(_translate("MainWindow", "Load existing model file"))
        self.label_6.setText(_translate("MainWindow", "Grab frames"))
        self.label_7.setText(_translate("MainWindow", "IP:"))

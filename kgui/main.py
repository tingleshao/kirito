import cv2
import os
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import grab_tools.grab as grab
import kgui.kirito_gui as kirito_gui
import stitching

#TODO: rename image name to 1-19


class MainWindow(QMainWindow, kirito_gui.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton2.clicked.connect(self.button2Clicked)

    def buttonClicked(self):
        if self.grabFrameCheckBox.isChecked():
            ip = self.ipLabel.text()
            grab.grab_with_v2(ip)
            # TODO: rename image name to 1-19
        threshold = self.horizontalSlider.tickPosition()
        if self.loadModelCheckBox.isChecked():
            stitching.stitching_pure_hugin(threshold)
        else:
            stitching.stitching_pure_hugin_without_existing_model(threshold)
        self.label.setPixmap(QtGui.QPixmap("preview.jpg"))

    def button2Clicked(self):
        stitching.preview_hugin()
        os.system("convert preview.jpg -resize 608x421 preview.jpg")
        self.label.setPixmap(QtGui.QPixmap("preview.jpg"))

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
 main()

import cv2
import os
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import getpass
import grab_tools.grab as grab
import kgui.kirito_gui as kirito_gui
import stitching

# TODO: make sure the frames are in order 
class MainWindow(QMainWindow, kirito_gui.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton2.clicked.connect(self.button2Clicked)
        self.pushButton3.clicked.connect(self.button3Clicked)
        username = getpass.getuser()
        self.dirLabel.setText("/home/"+username+"/data/stitching/foo")
        # link the "use pre-calibrated" checkbox
        self.loadModelCheckBox.stateChanged.connect(lambda x : self.enable_slot() if x else self.disable_slot())
        self.prealigned_pto_path = ""
        self.work_dir = ""

    def buttonClicked(self):
        if self.customDirCheckBox.isChecked():
            self.work_dir = self.dirLabel.text()
        elif self.work_dir == "":
            self.work_dir = stitching.prepare_directory()
        if self.grabFrameCheckBox.isChecked():
            ip = self.ipLabel.text()
            trials = 0
            while trials < 5:
                grab.grab_with_v2(ip, self.work_dir)
                n = grab.count_frames(self.work_dir)
                if n == 19: # make sure we get all 19 frames
                    break
            if trials == 5:
                print("error! failed to get frames after trying {0} times.".format(trails))
                return
            grab.move_frames(self.work_dir)
        # Stitch frames
        threshold = self.horizontalSlider.tickPosition()
        if self.loadModelCheckBox.isChecked():
            if self.prealigned_pto_path == "":
                self.prealigned_pto_path = QFileDialog.getOpenFileName()[0]
            # copy the prealigned model file to the working directory, and rename it as prealigned.pto
            os.system("cp {0} {1}/prealigned.pto".format(self.prealigned_pto_path, self.work_dir))
            stitching.stitching_pure_hugin(threshold, self.work_dir, self.maxVisScaleLabel.text(), self.radialLabel.text())
        else:
            stitching.stitching_pure_hugin_without_existing_model(threshold, self.work_dir, self.maxVisScaleLabel.text(), self.radialLabel.text())
        self.label.setPixmap(QtGui.QPixmap("{0}/preview.jpg".format(self.work_dir)))

    def button2Clicked(self):
        if self.customDirCheckBox.isChecked():
            self.work_dir = self.dirLabel.text()
        elif self.work_dir == "":
            self.work_dir = stitching.prepare_directory()
        stitching.preview_hugin()
        os.system("convert preview.jpg -resize 608x421 preview.jpg")
        self.label.setPixmap(QtGui.QPixmap("{0}/preview.jpg".format(self.work_dir)))

    def button3Clicked(self):
        if self.customDirCheckBox.isChecked():
            self.work_dir = self.dirLabel.text()
        elif self.work_dir == "":
            self.work_dir = stitching.prepare_directory()
        os.system("hugin {0}/optimized.pto".format(self.work_dir))

    def enable_slot(self):
        print("load existing model enabled")
        default_pto_file_path = "/home/" + getpass.getuser() + "/data/stitching/prealigned.pto"
        if not os.path.isfile(default_pto_file_path):
            print("File not found in default location. Need to select the prealigned pto file path")
            self.prealigned_pto_path = QFileDialog.getOpenFileName()[0]
        else:
            self.prealigned_pto_path = default_pto_file_path

    def disable_slot(self):
        print("load existing model disabled")


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
 main()

import cv2
import os
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import kgui.kirito_gui as kirito_gui


class MainWindow(QMainWindow, kirito_gui.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton2.clicked.connect(self.button2Clicked)

    def buttonClicked(self):
        os.system("./MantisGetFrames")
        print("stitching button clicked!")
        os.system("pto_gen mcam_*.jpeg -o test.pto")
    #    os.system("cpfind --prealigned --kdtreeseconddist=0.45 -o control_pts.pto init2.pto")
        os.system("cpfind --prealigned --kdtreeseconddist=0.45 -o control_pts.pto test.pto")
        # pruning control points
        #os.system("cpclean -o control_pts2.pto control_pts.pto")
        os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")
        os.system("linefind -o lines.pto pruning_pts.pto")
        # optimizing positions and geometry
        os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");
    #    os.system("hugin_executor -s optimized.pto -t 10")
    #    os.system("convert *.tif -resize 1500x500 output.jpg")
    #    os.system("rendering/Kirito_rendering 1021700000.jpg 1021700002.jpg 1021700004.jpg 1021700005.jpg 1021700006.jpg 1021700007.jpg 1021700008.jpg 1021700010.jpg 1021700010.jpg 1021700011.jpg 1021700014.jpg 1021700016.jpg 1021700018.jpg 1021700019.jpg 1021700021.jpg 1021700026.jpg 1031700003.jpg 1031700030.jpg 1021700012.jpg")
    #    os.system("rendering/Kirito_rendering mcam_1.jpeg mcam_2.jpeg")
        os.system("python3 update_pto_resolution.py")
        os.system("hugin_executor --stitching optimized.pto")
        os.system('convert "mcam_1 - mcam_19.tif" preview.jpg')
        self.label.setPixmap(QtGui.QPixmap("preview.jpg"))

    def button2Clicked(self):
        if not("preview.jpg" in os.listdir()):
            os.system("hugin_executor --stitching optimized.pto")
            os.system('convert "mcam_1 - mcam_19.tif" preview.jpg')
        self.label.setPixmap(QtGui.QPixmap("preview.jpg"))


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
 main()

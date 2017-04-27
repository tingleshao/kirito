import sys
import cv2
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
    #    self.pushButton2.clicked.connect(self.button2Clicked)
    #    self.broadcaster = data_broadcaster()
    #    self.index = 0
    #    self.packets = []
    #    if not testmode:
    #        self.camera = picamera.PiCamera()

    def buttonClicked(self):
        print("button clicked!")
        os.system("cpfind --prealigned --kdtreeseconddist=0.45 -o control_pts.pto init2.pto")

        # pruning control points
        #os.system("cpclean -o control_pts2.pto control_pts.pto")

        os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")

        os.system("linefind -o lines.pto pruning_pts.pto")

        # optimizing positions and geometry
        os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");
        os.system("hugin_executor -s optimized.pto")

def main():
    # read input image path
 #   shifted = cv2.pyrMeanShiftFiltering(image, 21, 51
#    segmenter = image_segmenter()
#    segmenter.watershed(shifted)
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
#    form.horizontalSlider_3.setProperty("value", 0)
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
 main()

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

    def buttonClicked(self):
        print("stitching button clicked!")
        os.system("cpfind --prealigned --kdtreeseconddist=0.45 -o control_pts.pto init2.pto")
        # pruning control points
        #os.system("cpclean -o control_pts2.pto control_pts.pto")
        os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")
        os.system("linefind -o lines.pto pruning_pts.pto")
        # optimizing positions and geometry
        os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");
        os.system("hugin_executor -s optimized.pto")

def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
 main()

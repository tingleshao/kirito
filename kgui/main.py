#import cv2
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
import json
import utils.utils as utils


# TODO: may combine some duplicated code
class MainWindow(QMainWindow, kirito_gui.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.stitchingButton.clicked.connect(self.stitchingButtonClicked)
        self.previewButton.clicked.connect(self.previewButtonClicked)
        self.huginButton.clicked.connect(self.huginButtonClicked)
        self.restitchingButton.clicked.connect(self.restitchingButtonClicked)
        self.ptoButton.clicked.connect(self.ptoButtonClicked)
        self.colorAdjustButton.clicked.connect(self.colorAdjustButtonClicked)
        username = getpass.getuser()
        # Change default dir here
        self.default_dir = "/home/"+username+"/mantisModelGen"
        self.dirLabel.setText(self.default_dir)
        # link the "use pre-calibrated" checkbox
        self.loadModelCheckBox.stateChanged.connect(lambda x : self.enable_slot() if x else self.disable_slot())
        self.prealigned_pto_path = ""
        self.work_dir = ""
        self.currReferencePtoDirLabel.setText("ref pto file: {0}".format(self.read_curr_ref_pto_file_location()))
        self.test = False


    def setTest(self):
        self.test = True


    def stitchingButtonClicked(self):
        self.work_dir = stitching.prepare_directory(self.default_dir)
        if self.grabFrameCheckBox.isChecked():
            ip = self.ipLabel.text()
            if self.test:
                grab.grab_mock(ip, self.work_dir)
            else:
                trials = 0
                while trials < 5:
                    result = grab.grab_with_v2(ip, self.work_dir)
                    if result == 1:
                        # cannot connect to V2
                        self.showErrorMsg("Cannot co  nnect to V2.")
                        trials = 6
                        break;
                    n = grab.count_frames(self.work_dir)
                    if n == 19: # make sure we get all 19 frames
                        break
                if trials == 5:
                    print("error! failed to get frames after trying {0} times.".format(trials))
                    return
                grab.move_frames(self.work_dir)
        # Stitch frames
        threshold = self.horizontalSlider.tickPosition()
        if self.loadModelCheckBox.isChecked():
            if self.prealigned_pto_path == "":
                dlg = self.getFilenameDialog()
                if dlg.exec_():
                    the_path = dlg.selectedFiles()[0]
                self.prealigned_pto_path = the_path
            # copy the prealigned model file to the working directory, and rename it as prealigned.pto
            self.currReferencePtoDirLabel.setText("ref pto file: " + self.prealigned_pto_path)
            stitching.update_saved_reference_pto_file_location(self.prealigned_pto_path)
            os.system("cp {0} {1}/prealigned.pto".format(self.prealigned_pto_path, self.work_dir))
            stitching.stitching_pure_hugin(threshold, self.work_dir, self.maxVisScaleLabel.text(), self.radialLabel.text())
        else:
            stitching.stitching_pure_hugin_without_existing_model(threshold, self.work_dir, self.maxVisScaleLabel.text(), self.radialLabel.text())
        self.label.setPixmap(QtGui.QPixmap("{0}/preview.jpg".format(self.work_dir)))

    def previewButtonClicked(self):
        if self.work_dir == "":
            self.work_dir = stitching.prepare_directory(self.default_dir)
        stitching.preview_hugin(self.work_dir)
        cwd = os.getcwd()
        os.chdir(self.work_dir)
        os.system("convert preview.jpg -resize 608x421 preview.jpg")
        self.label.setPixmap(QtGui.QPixmap("{0}/preview.jpg".format(self.work_dir)))
        os.chdir(cwd)


    def huginButtonClicked(self):
        if self.work_dir == "":
            self.work_dir = stitching.prepare_directory(self.default_dir)
        os.system("hugin {0}/optimized.pto".format(self.work_dir))
        updated_pto_file_name = stitching.check_updated_pto_file(self.work_dir)
        utils.clean_file("{0}/{1}".format(self.work_dir, updated_pto_file_name))
        self.currReferencePtoDirLabel.setText("ref pto file: {0}/{1}".format(self.work_dir, updated_pto_file_name))
        #remember this working directory and the updated pto file name.
        stitching.update_saved_reference_pto_file_location("{0}/{1}".format(self.work_dir, updated_pto_file_name))
        self.restitchingButton.setEnabled(True)


# TODO: restitching does not need grabbing frames
    def restitchingButtonClicked(self):
        # directly run the stitching again after open->close the Hugin application
        reference_pto_file_location = self.read_curr_ref_pto_file_location()
        #if self.customDirCheckBox.isChecked():
        #    self.work_dir = self.dirLabel.text()
        #elif self.work_dir == "":
        self.work_dir = stitching.prepare_directory(self.default_dir)
        if self.grabFrameCheckBox.isChecked():
            if self.test:
                grab.grab_mock(ip, self.work_dir)
            else:
                trials = 0
                while trials < 5:
                    result = grab.grab_with_v2(ip, self.work_dir)
                    if result == 1:
                        # cannot connect to V2
                        self.showErrorMsg("Cannot co  nnect to V2.")
                        trials = 6
                        break;
                    n = grab.count_frames(self.work_dir)
                    if n == 19: # make sure we get all 19 frames
                        break
                if trials == 5:
                    print("error! failed to get frames after trying {0} times.".format(trials))
                    return
                grab.move_frames(self.work_dir)
        # Stitch frames
        threshold = self.horizontalSlider.tickPosition()
        # copy the prealigned model file to the working directory, and rename it as prealigned.pto
        os.system("cp {0} {1}/prealigned.pto".format(reference_pto_file_location, self.work_dir))
        stitching.stitching_pure_hugin(threshold, self.work_dir, self.maxVisScaleLabel.text(), self.radialLabel.text())
        self.label.setPixmap(QtGui.QPixmap("{0}/preview.jpg".format(self.work_dir)))

    def ptoButtonClicked(self):
        dlg = self.getFilenameDialog()
        if dlg.exec_():
            the_path = dlg.selectedFiles()[0]
        if the_path != "":
            self.prealigned_pto_path = the_path
            self.currReferencePtoDirLabel.setText("ref pto file: " + self.prealigned_pto_path)
            stitching.update_saved_reference_pto_file_location(self.prealigned_pto_path)

    def colorAdjustButtonClicked(self):
        # color adjust
        stitching.match_color(self.work_dir, self.work_dir)

    def enable_slot(self):
        print("load existing model enabled")
        default_pto_file_path = self.read_curr_ref_pto_file_location()
        if default_pto_file_path == "N/A":
            self.showErrorMsg("the refernce pto file is N/A.")
            self.loadModelCheckBox.setCheckState(0)
            return
        self.prealigned_pto_path = default_pto_file_path

    def disable_slot(self):
        print("load existing model disabled")

    def read_curr_ref_pto_file_location(self):
        config_file_location = "reference_pto_file_location.json"
        has_config_file = os.path.isfile(config_file_location)
        if not has_config_file:
            return "N/A"
        with open('reference_pto_file_location.json') as data_file:
            data = json.load(data_file)
            return data["pto_file_location"]

    def showErrorMsg(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def getFilenameDialog(self):
        dlg = QFileDialog()
        dlg.setNameFilters(["Text files (*.txt)", "Hugin files (*.pto)"])
        dlg.setNameFilters(["Hugin files (*.pto)"])
        return dlg


def main(test=False):
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    if test:
        form.setTest()
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
   main()

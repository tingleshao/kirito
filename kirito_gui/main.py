import sys
import cv2
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import kirito_gui

'''
# always seem to need this
import sys
import cv2
# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from image_segmenter import image_segmenter
import argparse as ap
# This is our window from QtCreator
import mainwindow_auto
from image_encoder import image_encoder
from data_broadcaster import data_broadcaster
import time, threading
from tri_encoder import tri_encoder

testmode = False
if len(sys.argv) > 1:
    testmode = True

if not testmode:
    import picamera
    import RPi.GPIO as gp

import numpy as np
import os


# TODO: good segemntation + open source license etc.

#gp.setwarnings(False)
#gp.setmode(gp.BOARD)
#gp.setup(7, gp.OUT)
#gp.setup(11, gp.OUT)
#gp.setup(12, gp.OUT)

#gp.output(11, True)
#gp.output(12, True)


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton2.clicked.connect(self.button2Clicked)
        self.broadcaster = data_broadcaster()
        self.index = 0
        self.packets = []
        if not testmode:
            self.camera = picamera.PiCamera()

    def buttonClicked(self):
        if not testmode:
            sender = self.sender()
            self.statusBar().showMessage(sender.text() + ' was pressed')
        #    image = cv2.imread("image.jpg")
        #    encoder = image_encoder()
        #    img_data, encoded_img_data = encoder.encode(image)
        #    cv2.imshow("output", encoder.decode(img_data))
        #    print(encoded_img_data)
            if self.radio_1.isChecked():
                self.set_data(self.encoded_img_data)
                print("broadcasting gray image")
            elif self.radio_2.isChecked():
                self.set_data(self.encoded_img_data_color)
                print("broadcasting color image")
            elif self.checkbox_tri.isChecked():
                self.set_data(self.encoded_img_data_tri)
                print("broadcasting tri image")
            print("self data:" + str(self.data))
            encoder = image_encoder()
            self.packets = encoder.prepare(self.data)
            self.index = 0
            self.broadcast_image()
        print("button clicked!")

# if capture image button is clicked
    def button2Clicked(self):
#        gp.output(7, False)
#        gp.output(11, False)
#        gp.output(12, True)
        if not testmode:
            self.camera.start_preview(fullscreen=False, window=(10,20,640,480))
            signal = input()
            self.camera.stop_preview()
            self.camera.close()
            self.capture()
      #  gp.setwarnings(False)
      #  gp.setmode(gp.BOARD)

      #  gp.setup(7, gp.OUT)
      #  gp.setup(11, gp.OUT)
      #  gp.setup(12, gp.OUT)

     #   gp.output(11, True)
     #   gp.output(12, True)

 #       gp.output(7, False)
 #       gp.output(11, False)
 #       gp.output(12, True)    #    self.camera.capture("image.jpg")
 #       self.capture(1)

 #       gp.output(7, False)
 #       gp.output(11, True)
 #       gp.output(12, False)
 #       self.capture(3)
   #     gp.output(7, False)
   #     gp.output(11, False)
   #     gp.output(12, True)
            image1 = cv2.imread("capture_1.jpg")
            image2 = cv2.imread("capture_3.jpg")
            image1 = image1[:,324:2267]
            image2 = image2[:,324:2267]
            image1 = cv2.resize(image1, (200,200), interpolation=cv2.INTER_CUBIC)
            image2 = cv2.resize(image2, (200,200), interpolation=cv2.INTER_CUBIC)
        if testmode:
            image = cv2.imread("capture_1x.png")
        else:
            image = cv2.imread("capture_1.jpg")
            image = image[:, 324:2267]
                     #   image2 = cv2.imread("capture_3.jpg")
        segmenter = image_segmenter()
        if self.checkbox_seg.isChecked():
            image = segmenter.disparity(image1, image2)
    #        cv2.imwrite("seg.png", image)
  #      segmenter.watershed(image1)
        encoder = image_encoder()
        t_encoder = tri_encoder()

        # DCT encode image
    #    img_data, self.encoded_img_data = encoder.encode(image, True)
    #    img_datar, img_datag, img_datab, self.encoded_img_data_color = encoder.encode_color(image, True)
        # TODO: here switch to using constraint
        grey_constraint_index, color_constraint_index, tri_constraint_index = self.find_index()
        img_data, self.encoded_img_data = encoder.encode_with_constraint(image, grey_constraint_index)
        img_datar, img_datag, img_datab, self.encoded_img_data_color = encoder.encode_color_with_constraint(image, color_constraint_index)

        self.decoded_image = encoder.decode(img_data) * 255.0
        self.decoded_image = self.decoded_image - np.amin(self.decoded_image)
        self.decoded_imager = encoder.decode(img_datar) * 255.0
        self.decoded_imageg = encoder.decode(img_datag) * 255.0
        self.decoded_imageb = encoder.decode(img_datab) * 255.0
        self.decoded_imager = self.decoded_imager - np.amin(self.decoded_imager)
        self.decoded_imageg = self.decoded_imageg - np.amin(self.decoded_imageg)
        self.decoded_imageb = self.decoded_imageb - np.amin(self.decoded_imageb)

        self.decoded_image_color = np.zeros((64,64,3), np.uint8)
        self.decoded_image_color[:,:,0] = self.decoded_imager
        self.decoded_image_color[:,:,1] = self.decoded_imageg
        self.decoded_image_color[:,:,2] =  self.decoded_imageb
#        self.decoded_image_colo = self.decoded_imager - np.amin(self.decoded_image_color)
        print("decoded_image " + str(self.decoded_image))
        print("decodecd_image_color" + str(self.decoded_image_color))
    #    cv2.imshow("output", encoder.decode(img_data))
        cv2.imwrite("gray.jpg", self.decoded_image)
        cv2.imwrite("color.jpg", self.decoded_image_color)
        self.label_10.setPixmap(QtGui.QPixmap("gray.jpg"))
        self.label_11.setPixmap(QtGui.QPixmap("color.jpg"))
        if self.checkbox_tri.isChecked():
        # triangle encode image
            cv2.imwrite("capture_1tri.jpg", image1);
            tri_filename = "capture_1tri.jpg"
            if testmode:
                self.encoded_img_data_tri = t_encoder.encode(image, True, tri_filename, tri_constraint_index)
            else:
                self.encoded_img_data_tri = t_encoder.encode(image, False, tri_filename, tri_constraint_index)
    #        encoded_str = ""
    #        for i in encoded_img_data_tri:
    #            encoded_str = encoded_str + str(int(i)) + " "
    #        print(encoded_str)
        #    print(encoded_img_data_tri)
            print("tri data len: " + str(len(self.encoded_img_data_tri)))
            print("delaunay_" + tri_filename)
            image = QtGui.QImage("delaunay_" + tri_filename)
            a = cv2.imread("autocontrasted_delaunay_" + "capture_1tri.jpg")
            b = cv2.resize(a, (64,64))
            cv2.imwrite("tri.jpg", b)
    #        self.label_11.setPixmap(QtGui.QPixmap("delaunay_" + "capture_1x.jpg"))
            self.label_12.setPixmap(QtGui.QPixmap("tri.jpg"))
            print("here")

    def capture(self):
        cmd = "python3 test_cam.py"
        os.system(cmd)

    def set_data(self, data):
        self.data = data

    def broadcast_image(self):
        print("packets"+ str(self.packets))
        print("index"+str(self.index))
        self.broadcaster.broadcast_data(self.packets[self.index])
        self.index = self.index +1
        if self.index >= len(self.packets):
            self.index = 0
        threading.Timer(1.3, self.broadcast_image ).start()

 #TODO: finish this
    def find_index(self):
        # for threshold 30, the time is gray: 10s, color: 40s
        delay = self.horizontalSlider_2.value()
        lifetime = self.horizontalSlider.value()
        if delay > 90:
            return 60, 60, 2.1
        elif delay >= 66:
            return 60, 30, 1.8
        elif delay > 33:
            return 40, 20, 1.6
        else:
            return 30, 10, 1.4
    #    print("life time / delay: " + str(lifetime) + " " + str(delay))
    #    return 1,2,3


def main():
    # read input image path
 #   shifted = cv2.pyrMeanShiftFiltering(image, 21, 51
#    segmenter = image_segmenter()
#    segmenter.watershed(shifted)
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.horizontalSlider_3.setProperty("value", 0)
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
 main()
''' 


class MainWindow(QMainWindow, kirito_gui.Ui_MainWindow):
    # access variables inside of the UI's file
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
    #    self.pushButton.clicked.connect(self.buttonClicked)
    #    self.pushButton2.clicked.connect(self.button2Clicked)
    #    self.broadcaster = data_broadcaster()
    #    self.index = 0
    #    self.packets = []
    #    if not testmode:
    #        self.camera = picamera.PiCamera()


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

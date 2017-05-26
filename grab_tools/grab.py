# grab frames using mantis API
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys, time
#from pcvform import Ui_PyCamViewer as UI
from PIL import Image
from PIL.ImageQt import ImageQt

#import MantisPyAPI as mantis

try:
    from PySide import QtCore, QtWidgets
except:
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5 import QtCore, QtWidgets, QtGui


def startServer(start):
    print("h6")

    if start:
        # --- Connect to the camera ---
        print("ipaddress:" + str(ipAddress))
        mantis.mCamConnect(ipAddress, 9999)
        print("hi8")
    else:
        # --- Disconnect from the camera ---
        mantis.mCamDisconnect(ipAddress, 9999);


def call(meta, jpeg):
    print("call get called")
    image = ImageQt(jpeg)
    image = image.convertToFormat(QtGui.QImage.Format_RGB888)
    image.save("test.jpg", 'jpg')
    newImage.emit(meta, image)


def newMcam(mcamhandle):
    if not mhandle:
        mhandle = mcamhandle

def count_frames(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(f) and len(f.split(".")) > 1 and (f.split(".")[1] == 'jpeg' or f.split(".")[1] == 'jpg') and not f == "preview.jpg"]
    return len(files)

def grab(start):
    print("ipaddress:" + str(ipAddress))
    mantis.mCamConnect(ipAddress, 9999)
    print("start" + str(start))
    print("mhandle" + str(mhandle))
    print("here")
    frame = mantis.grabMCamFrame(9999, 1.0)
    print("her2")
#    frame.save("test.jpg", 'jpg')
    mantis.mCamDisconnect(ipAddress, 9999);
    # --- Start streaming ---
    #    mantis.startMCamStream(mcamhandle, 9002)
    # --- Only receive HD ---
    #    mantis.setMCamStreamFilter(mcamhandle, 9002, mantis.ATL_SCALE_MODE_HD)
#    elif mhandle:
        # --- Start streaming ---
#        mantis.stopMCamStream(mcamhandle, 9002)


def grab_with_v2(ip, directory):
    os.system("grab_tools/MantisGetFrames -ip " + ip)
    os.system("mkdir " + directory)
    os.system("cp *.jpeg " + directory)


def rename_frames():
    # rename frames to 1...19 jpeg
    files = [f for f in os.listdir('.') if os.path.isfile(f) and len(f.split(".")) > 1 and (f.split(".")[1] == 'jpeg' or f.split(".")[1] == 'jpg') and not f == "preview.jpeg"]
    # rename files
    print("files: " + str(files))
    new_file_names = [str(i) + ".jpeg" for i in range(19)]
    print("new file names; " + str(new_file_names))
    curr_index = 0
    for f in files:
        print(curr_index)
        os.system("mv " + f + " " + new_file_names[curr_index])
        curr_index = curr_index + 1
        # avoid index out of bounds error
        if curr_index == 19:
            break

def move_frames(work_dir):
    # rename frames to 1...19 jpeg
    os.system("mv *.jpeg {0}".format(work_dir))


def existing():
    grab(False)
    startServer(False)
    time.sleep(0.2)
    mantis.closeMCamFrameReceiver(9002)


def main():
    grab(True)
    existing()

if __name__ == "__main__":
    main()

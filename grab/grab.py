# grab frames using mantis API
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, time
from pcvform import Ui_PyCamViewer as UI
from PIL import Image
from PIL.ImageQt import ImageQt
import MantisPyAPI as mantis

try:
    from PySide import QtCore, QtWidgets
except:
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5 import QtCore, QtWidgets, QtGui


newImage = QtCore.pyqtSignal(api.FRAME_METADATA, 'QImage')
newImage.connect(receiveImage)
mcamhandle = None
ipAddress = None
api.initMCamFrameReceiver(9002, 1)
api.setMCamFrameCallback(call)
# --- Set the new mcam callback ---
api.setNewMCamCallback(newMcam)


def startServer(self, start):
    if start:
        ipAddress = "10.0.0.173"
        # --- Connect to the camera ---
        api.mCamConnect(ipAddress, 9999)
    else:
        # --- Disconnect from the camera ---
        api.mCamDisconnect(ipAddress, 9999);


def call(self, meta, jpeg):
    image = ImageQt(jpeg)
    image = image.convertToFormat(QtGui.QImage.Format_RGB888)
    self.newImage.emit(meta, image)


def newMcam(self, mcamhandle):
    if not self.mcamhandle:
        self.mcamhandle = mcamhandle


def grab():
    if start and mcamhandle:
        # --- Start streaming ---
        api.startMCamStream(mcamhandle, 9002)
        # --- Only receive HD ---
        api.setMCamStreamFilter(mcamhandle, 9002, api.ATL_SCALE_MODE_HD)
    elif mcamhandle:
        # --- Start streaming ---
        api.stopMCamStream(mcamhandle, 9002)


def main():
    grab()


if __name__ == "__main__":
    main()

import MantisPyAPI as api

# init receiver
print("init receiver")
api.initMCamFrameReceiver(9002, 1)
ipAddress = "10.0.0.173"
port = 9999
print("connect")
api.mCamConnect(ipAddress, port)
print("grab frame")
frame = api.grabMCamFrame(9999, 1.0)

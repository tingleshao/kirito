import MantisPyAPI as api


def getCameraId(ip, port):
    cameras = []
    api.cameraConnect(ip, port)
    numCameras = api.getNumberOfCameras()
    api.setNewCameraCallback(lambda x: cameras.append(x))
    for camera in cameras:
        print("Found camera with ID "\
                + str(camera.camID) + " and "\
                + str(camera.numMCams) + " microcameras")
    for camera in cameras:
        api.disconnectCamera(camera)
    if len(cameras) > 0:
        return caemras[0].camID
    return -1


def main():
    print("main")


if __name__ == "__main__":
    main()

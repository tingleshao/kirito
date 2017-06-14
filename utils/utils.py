import os
import sys

import MantisPyAPI as api


def update_crop_factor(filename):
    with open(filename) as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ""
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if line == "#-hugin  cropFactor=1":
            output_str  = output_str + "#-hugin  cropFactor=7" + '\n'
        else:
            output_str = output_str + line + '\n'
        curr_idx = curr_idx + 1
    with open("init2.pto", 'w') as output_file:
        output_file.write(output_str)


def update_cf_and_v_assuming_cam4():
    filename = sys.argv[1]
    with open(filename) as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ""
    updated_v = False
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if line == "#-hugin  cropFactor=1":
            output_str  = output_str + "#-hugin  cropFactor=7" + '\n'
        elif not updated_v and len(line) > 20 and line[0:20] == "i w3840 h2160 f0 v50":
            output_str = output_str + "i w3840 h2160 f0 v12.299017381458" + line[20:] + '\n'
            updated_v = True
        elif len(line) > 20 and line[-9:-1] == "418.jpeg":
            output_str = output_str + "i w3840 h2160 f0 v75.1633550117801 Ra0 Rb0 Rc0 Rd0 Re0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a0 b0 c0 d0 e0 g0 t0 Va1 Vb0 Vc0 Vd0 Vx0 Vy0  Vm5 n\"418.jpeg\"" + '\n'
        else:
            output_str = output_str + line + '\n'
        curr_idx = curr_idx + 1
    with open("init2.pto", 'w') as output_file:
        output_file.write(output_str)


def change_filename():
    idx_map = [13, 14, 15, 16, 17, 18, 12, 1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6]
    for i in range(18):
        for j in range(3):
            os.system("cp ../frame_0_copy/mcam_{0}_scale_{1}.jpg mcam_{2}_scale_{3}.jpg".format(i+1, j, idx_map[i], j))


# update the resolution in a pto file.
def update_pto_resolution():
    with open("optimized_centered.pto") as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ''
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if len(line) > 0 and line[0] == "p":
            tokens = line.split(" ")
            width = int(tokens[2][1:])
            height = int(tokens[3][1:])
            new_width = str(width / 10)
            new_height = str(height / 10)
            new_line = "p " + tokens[1] + " w" + new_width + " h" + new_height + " " + " ".join(tokens[4:])
            output_str = output_str + new_line + "\n"
        else:
            output_str = output_str + line + "\n"
        curr_idx = curr_idx + 1
    with open("optimized_s.pto", 'w') as output_file:
        output_file.write(output_str)


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


# adjust the order of the cameras in an pto file, try to get the best possbile
# stitching result
def adjust_order_for_mantis_cam4(input_pto_file_name, output_pto_file_name):
    with open(input_pto_file_name) as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    cam_info_dict = {}
    output_str = ""
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if len(line) > 20 and line[-6:-1] == ".jpeg":
            cam_info_dict[line[-9:-1].split(".")[0]] = line
        curr_idx = curr_idx + 1
    curr_idx = 0
    curr_idx_for_cam = 0
    cam_list = ["410","409","408","407","406","400","401","402","403","404","405","411","417","416","415","414","413","412","418"]
    # rewrite pto file
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if len(line) > 20 and line[-6:-1] == ".jpeg":
            output_str = output_str + cam_info_dict[cam_list[curr_idx_for_cam]] + "\n"
        else:
            output_str = output_str + line + "\n"
    # write output
    with open("output_pto_file_name", 'w') as output_file:
        output_file.write(output_str)

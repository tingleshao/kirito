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


def clean_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    lines = text.split('\n')
    curr_idx = 0
    output_str = ""
    while curr_idx < len(lines):
        line = lines[curr_idx]
        if len(line) > 0 and (line[0] == "v" or line[0] == "c"):
            output_str = output_str + ""
        elif len(line) > 0 and line == "# specify variables that should be optimized":
            output_str = output_str + line + "\n" + "v" + "\n"
        else:
            output_str = output_str + line + "\n"
        curr_idx = curr_idx + 1
    with open(filename, 'w') as output_file:
        output_file.write(output_str)


def generate_hugin_input():
    output = '''# pto project file generated by Hugin's cpfind

# hugin project file
#hugin_ptoversion 2
p f2 w3000 h1500 v73  E0 R0 n"TIFF_m c:LZW r:CROP"
m g1 i0 f0 m2 p0.00784314

# image lines
#-hugin  cropFactor=7
i w3840 h2160 f0 v12.3 Ra0 Rb0 Rc0 Rd0 Re0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a0 b0 c0 d0 e0 g0 t0 Va1 Vb0 Vc0 Vd0 Vx0 Vy0  Vm5 n"mcam_1_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_2_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_3_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_4_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_5_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_6_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_7_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_8_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_9_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_10_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_11_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_12_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_13_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_14_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_15_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_16_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_17_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_18_scale_2.jpg"


# specify variables that should be optimized
v'''

    with open('parsed_output_for_hugin.txt') as feature_info_file:
        feature_info = feature_info_file.read()

    output = output + '\n\n'
    output = output + feature_info
    output = output + '''

#hugin_optimizeReferenceImage 0
#hugin_blender enblend
#hugin_remapper nona
#hugin_enblendOptions
#hugin_enfuseOptions
#hugin_hdrmergeOptions
#hugin_verdandiOptions
#hugin_outputLDRBlended true
#hugin_outputLDRLayers false
#hugin_outputLDRExposureRemapped false
#hugin_outputLDRExposureLayers false
#hugin_outputLDRExposureBlended false
#hugin_outputLDRStacks false
#hugin_outputLDRExposureLayersFused false
#hugin_outputHDRBlended false
#hugin_outputHDRLayers false
#hugin_outputHDRStacks false
#hugin_outputLayersCompression LZW
#hugin_outputImageType tif
#hugin_outputImageTypeCompression LZW
#hugin_outputJPEGQuality 100
#hugin_outputImageTypeHDR exr
#hugin_outputImageTypeHDRCompression LZW
#hugin_outputStacksMinOverlap 0.7
#hugin_outputLayersExposureDiff 0.5
#hugin_optimizerMasterSwitch 1
#hugin_optimizerPhotoMasterSwitch 21
'''

    with open('test0.pto', 'w') as pto_file:
        pto_file.write(output)


def generate_hugin_input2():
    output = '''# pto project file generated by Hugin's cpfind

# hugin project file
#hugin_ptoversion 2
p f2 w3000 h1500 v73  E0 R0 n"TIFF_m c:LZW r:CROP"
m g1 i0 f0 m2 p0.00784314

# image lines
#-hugin  cropFactor=7
i w3840 h2160 f0 v12.3 Ra0 Rb0 Rc0 Rd0 Re0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a0 b0 c0 d0 e0 g0 t0 Va1 Vb0 Vc0 Vd0 Vx0 Vy0  Vm5 n"mcam_1_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_2_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_3_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_4_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_5_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_6_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_7_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_8_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_9_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_10_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_11_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_12_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_13_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_14_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_15_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_16_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_17_scale_2.jpg"
#-hugin  cropFactor=7
i w3840 h2160 f0 v=0 Ra=0 Rb=0 Rc=0 Rd=0 Re=0 Eev0 Er1 Eb1 r0 p0 y0 TrX0 TrY0 TrZ0 Tpy0 Tpp0 j0 a=0 b=0 c=0 d=0 e=0 g=0 t=0 Va=0 Vb=0 Vc=0 Vd=0 Vx=0 Vy=0  Vm5 n"mcam_18_scale_2.jpg"


# specify variables that should be optimized
v'''

    with open('parsed_output_for_hugin.txt') as feature_info_file:
        feature_info = feature_info_file.read()

    output = output + '\n\n'
    output = output + feature_info
    output = output + '''

#hugin_optimizeReferenceImage 0
#hugin_blender enblend
#hugin_remapper nona
#hugin_enblendOptions
#hugin_enfuseOptions
#hugin_hdrmergeOptions
#hugin_verdandiOptions
#hugin_outputLDRBlended true
#hugin_outputLDRLayers false
#hugin_outputLDRExposureRemapped false
#hugin_outputLDRExposureLayers false
#hugin_outputLDRExposureBlended false
#hugin_outputLDRStacks false
#hugin_outputLDRExposureLayersFused false
#hugin_outputHDRBlended false
#hugin_outputHDRLayers false
#hugin_outputHDRStacks false
#hugin_outputLayersCompression LZW
#hugin_outputImageType tif
#hugin_outputImageTypeCompression LZW
#hugin_outputJPEGQuality 100
#hugin_outputImageTypeHDR exr
#hugin_outputImageTypeHDRCompression LZW
#hugin_outputStacksMinOverlap 0.7
#hugin_outputLayersExposureDiff 0.5
#hugin_optimizerMasterSwitch 1
#hugin_optimizerPhotoMasterSwitch 21
'''

    with open('test0.pto', 'w') as pto_file:
        pto_file.write(output)

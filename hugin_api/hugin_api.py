# Hugin API
import os
import cv2


def hugin_find_features(image_names):
    image_names_str = " ".join(image_names)
    os.system("pto_gen {0} -o temp.pto".format(image_names_str))
    os.system("cpfind --multirow -o temp_control_pts.pto temp.pto")
    kp = load_control_points("temp_control_pts.pto")
    os.system("rm temp.pto")
    # return key point location and descriptor?
    return kp


def hugin_find_matches(image_names):
    image_names_str = " ".join(image_names)
    os.system("pto_gen {0} -o temp.pto".format(image_names_str))
    os.system("cpfind --multirow -o temp_control_pts.pto temp.pto")
    matches = load_matches("temp_control_pts.pto")
#    os.system("rm temp.pto")
    # return key point location and descriptor?
    return matches


def load_matches(pto_name):
    with open(pto_name) as pto_file:
        pto = pto_file.read()
    pts_list = []
    lines = pto.split("\n")
    pts_list = list(filter(lambda x: len(x) > 1 and x[0] == 'c', lines))
    cam1_pts = []
    cam2_pts = []
    matches = []
    for pts in pts_list:
        tokens = pts.split(" ")
        cam1_pt = (float(tokens[3][1:]), float(tokens[4][1:]))
        cam2_pt = (float(tokens[5][1:]), float(tokens[6][1:]))
        if cam1_pt in cam1_pts:
            pt1_idx = cam1_pts.index(cam1_pt)
        else:
            pt1_idx = len(cam1_pts)
            cam1_pts.append(cam1_pt)
        if cam2_pt in cam2_pts:
            pt2_idx = cam2_pts.index(cam2_pt)
        else:
            pt2_idx = len(cam2_pts)
            cam2_pts.append(cam1_pt)
        dmatch = cv2.DMatch(pt1_idx, pt2_idx, 0)
        matches.append(dmatch)
    return matches, cam1_pts, cam2_pts


def load_control_points(pto_name):
    with open(pto_name) as pto_file:
        pto = pto_file.read()
    pts_list = []
    lines = pto.split("\n")
    kp_dict = {}
    pts_list = list(filter(lambda x: len(x) > 1 and x[0] == 'c', lines))
    for pts in pts_list:
        tokens = pts.split(" ")
        cam1_id = int(tokens[1][1:])
        cam2_id = int(tokens[2][1:])
        cam1_pt = (float(tokens[3][1:]), float(tokens[4][1:]))
        cam2_pt = (float(tokens[5][1:]), float(tokens[6][1:]))
        if not cam1_id in kp_dict.keys():
            kp_dict[cam_1_id] = [cam1_pt]
        else:
            kp_dict[cam_1_id].append(cam1_pt)
        if not cam2_id in kp_dict.keys():
            kp_dict[cam_2_id] = [cam2_pt]
        else:
            kp_dict[cam_2_id].append(cam2_pt)
        return kp_dict

def toKeyPoints(kps):
    # covert x, y pair to KeyPoint object

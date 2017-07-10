# Hugin API
import os


def hugin_find_features(image_names):
    image_names_str = " ".join(image_names)
    os.system("pto_gen {0} -o temp.pto".format(image_names_str))
    os.system("cpfind --multirow -o temp_control_pts.pto temp.pto")
    kp = load_control_points("temp_control_pts.pto")
    os.system("rm temp.pto")
    # return key point location and descriptor?
    return kp


def load_control_points(pto_name):
    with open(pto_name) as pto_file:
        pto = pto_file.read()
    pts_list = []
    lines = pto.split("\n")
    kp_dict = {}
    # TODO: this can be rewritten using a filter
    for line in lines:
        if len(line) > 1 and line[0] == 'c':
            pts_list.append(line)
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

# Hugin API
import os


def find_features(image_name):
    os.system("pto_gen {0} -o init.pto".format(image_name))
    os.system("cpfind --multirow -o control_pts.pto init2.pto")

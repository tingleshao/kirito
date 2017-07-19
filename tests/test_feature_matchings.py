# Given a pto file, we displays the features detected, to see what is going on
#
#
#
import sys
import os
from sys import platform
if platform == "darwin":
    sys.path.append('/Users/chongshao/dev/applications/stitching_app/rendering/')
    sys.path.append('/Users/chongshao/dev/applications/stitching_app/hugin_api/')
    sys.path.append('/Users/chongshao/dev/applications/stitching_app/')
if platform == "linux":
    sys.path.append('/home/cshao/dev/applications/stitching_app/rendering/')
    sys.path.append('/home/cshao/dev/applications/stitching_app/hugin_api/')
    sys.path.append('/home/cshao/dev/applications/stitching_app/')


import hugin_api
import matching_visualizer



def test():
    pto_file_name = "pruning_pts3.pto"
    camera1_id = 1
    camera2_id = 2
    currdir = os.getcwd()
    matching_visualizer.visualize_features_from_pto_files(currdir, pto_file_name, camera1_id, camera2_id)


if __name__ == "__main__":
    test()

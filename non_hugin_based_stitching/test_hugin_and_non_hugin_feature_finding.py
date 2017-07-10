# This script finds features using Hugin-based method and non-hugin based method.
# And displays the features in different colors
from numpy.misc import imread
import cv2
<<<<<<< HEAD
import sys
import numpy as np
sys.path.append('/Users/chongshao/dev/applications/stitching_app/rendering/')
sys.path.append('/Users/chongshao/dev/applications/stitching_app/hugin_api/')
sys.path.append('/Users/chongshao/dev/applications/stitching_app/')
import hugin_api
import matching_visualizer

import matplotlib.pyplot as plt

# TODO: 1. Make a warp to see the errors
# TODO: 2. Evaluate the performance on wide field of view camera
# TODO: 3. when features not found, load the referencer pto matches
# TODO: 4. Spherical warper testing: detail::SphericalWarper

def test_finding_features_image_pair(image_names):
    image1_name = image_names[0]
    image2_name = image_names[1]
    image1 = cv2.imread(image1_name)
    image2 = cv2.imread(image2_name)
=======
# TODO; implement this method
from matching_visualizer import visualize
from hugin_api.hugin_api import hugin_find_features


# def test_finding_features_image_pair(image_name):
#     image1 = imread(image1_name)
#     # find features using opencv
#     orb = cv2.ORB()
#     kp1, des1 = orb.detectAndCompute(img1, None)
#     kp2, des2 = hugin_find_features(img1)
#     visualize(kp1, "blue", kp2, "red")


def test_finding_features_image_pair(image_name1, image_name2):
#    image1_name = # XXX:
    image1 = imread(image1_name)
>>>>>>> e8519f3ed08f2863d12e460c548141085eb3c0eb
    # find features using opencv
    orb = cv2.ORB()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checkds=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    maches = flann.knnMatch(des1, des2, k2)
    visualize(maches)
    match_dict = hugin_find_features(img1)
    visualize(match_dict)


def test_finding_features_multiple_image_pairs():
    image_names = #XXX
    for image_name in image_names:
        test_finding_features_image_pair(image_name)


def test_warping_errors():
    # TODO: find matches using two methods and wrap the image (compute homography?)
    # Or another method used in the demo
    return None 


def main():
    image1_name = # XXX:
    image2_name = # XXX:
    test_finding_features_image_pair([image1_name, image2_name])


if __name__ == "__main__":
    main()

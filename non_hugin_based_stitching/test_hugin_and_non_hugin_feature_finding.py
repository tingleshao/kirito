# This script finds features using Hugin-based method and non-hugin based method.
# And displays the features in different colors
from numpy.misc import imread
import cv2
from matching_visualizer import visualize
# TODO: provide an interface from Hugin to Python to find features
from hugin_api import hugin_find_features


def test_finding_features_in_hugin_non_hugin_single_image(image_name):
#    image1_name = # XXX:
    image1 = imread(image1_name)
    # find features using opencv
    orb = cv2.ORB()
    kp1, des1 = orb.detectAndCompute(img1, None)
    visualize(kp1, "blue")
    kp2, des2 = hugin_find_features(img1)
    visualize(kp2, "red")


def test_finding_features_in_hugin_non_hugin_multiple_images():
    image_names = #XXX
    for image_name in image_names:
        test_finding_features_in_hugin_non_hugin_single_image(image_name)


def test_finding_features_and_matching_two_images(image_name1, image_name2):
#    image1_name = # XXX:
    image1 = imread(image1_name)
    # find features using opencv
    orb = cv2.ORB()
    kp1, des1 = orb.detectAndCompute(img1, None)
    visualize(kp1, "blue")
    kp2, des2 = hugin_find_features(img1)
    visualize(kp2, "red")
    


def test_findning_features_and_matching_multiple_images():
    return None

# This script finds features using Hugin-based method and non-hugin based method.
# And displays the features in different colors
from numpy.misc import imread
import cv2
# TODO; implement this method
from matching_visualizer import visualize
from hugin_api.hugin_api import hugin_find_features


def test_finding_features_image_pair(image_name):
    image1 = imread(image1_name)
    # find features using opencv
    orb = cv2.ORB()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = hugin_find_features(img1)
    visualize(kp1, "blue", kp2, "red")


def test_finding_features_multiple_image_pairs():
    image_names = #XXX
    for image_name in image_names:
        test_finding_features_image_pair(image_name)

#
# def test_finding_features_and_matching_two_images(image_name1, image_name2):
# #    image1_name = # XXX:
#     image1 = imread(image1_name)
#     # find features using opencv
#     orb = cv2.ORB()
#     kp1, des1 = orb.detectAndCompute(img1, None)
#     visualize(kp1, "blue")
#     kp2, des2 = hugin_find_features(img1)
#     visualize(kp2, "red")


def main():
    image1_name = # XXX:
    image2_name = # XXX:
    test_finding_features_image_pair([image1_name, image2_name])


if __name__ == "__main__":
    main()

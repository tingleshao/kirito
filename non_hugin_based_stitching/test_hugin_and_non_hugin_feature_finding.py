# This script finds features using Hugin-based method and non-hugin based method.
# And displays the features in different colors
from scipy.misc import imread
import cv2
import sys
import numpy as np
sys.path.append('/Users/chongshao/dev/applications/stitching_app/rendering/')
sys.path.append('/Users/chongshao/dev/applications/stitching_app/hugin_api/')
sys.path.append('/Users/chongshao/dev/applications/stitching_app/')
import hugin_api
import matching_visualizer

# def test_finding_features_image_pair(image_name):
#     image1 = imread(image1_name)
#     # find features using opencv
#     orb = cv2.ORB()
#     kp1, des1 = orb.detectAndCompute(img1, None)
#     kp2, des2 = hugin_find_features(img1)
#     visualize(kp1, "blue", kp2, "red")


def test_finding_features_image_pair(image_names):
    image1_name = image_names[0]
    image2_name = image_names[1]
    image1 = cv2.imread(image1_name)
    image2 = cv2.imread(image2_name)
    # find features using opencv
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(image1, None)
    kp2, des2 = orb.detectAndCompute(image2, None)
    des1 = np.float32(des1)
    des2 = np.float32(des2)
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checkds=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=1)
    for match in matches:
        print(match)
    matching_visualizer.visualize(matches, image1, image2, kp1, kp2)
    matches = hugin_find_matches(img1)
    matching_visualizer.visualize(matches, image1, image2, cam1_pts, cam2_pts)


def test_finding_features_multiple_image_pairs():
    image_names = "none"
    for image_name in image_names:
        test_finding_features_image_pair(image_name)


def main():
    image1_name = '../test_frames/1021700000.jpeg'
    image2_name = '../test_frames/1021700002.jpeg'
    test_finding_features_image_pair([image1_name, image2_name])


if __name__ == "__main__":
    main()

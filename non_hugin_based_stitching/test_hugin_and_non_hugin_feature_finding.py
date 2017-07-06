# This script finds features using Hugin-based method and non-hugin based method.
# And displays the features in different colors
from scipy.misc import imread
import cv2
import sys
sys.path.append('/Users/chongshao/dev/applications/stitching_app/rendering/')
sys.path.append('/Users/chongshao/dev/applications/stitching_app/hugin_api/')
import hugin_api
import matching_visualizer

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
    image_names = "none"
    for image_name in image_names:
        test_finding_features_image_pair(image_name)


def main():
    image1_name = 'test_frames/102170000.jpeg'
    image2_name = 'test_frames/102170002.jpeg'
    test_finding_features_image_pair([image1_name, image2_name])


if __name__ == "__main__":
    main()

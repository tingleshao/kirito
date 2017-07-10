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
import matplotlib.pyplot as plt



# TODO: 1. Make a warp to see the errors
# TODO: 2. Evaluate the performance on wide field of view camera
# TODO: 4. Spherical warper testing: detail::SphericalWarper
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
    print(matches)
    matches2, cam1_pts, cam2_pts = hugin_api.hugin_find_matches(image_names)
    print(matches2)
    cam1_pts = hugin_api.toKeyPoints(cam1_pts)
    cam2_pts = hugin_api.toKeyPoints(cam2_pts)
    matching_visualizer.visualize(matches, image1, image2, kp1, kp2)
    matching_visualizer.visualize(matches2, image1, image2, cam1_pts, cam2_pts)
    plt.show()


def test_finding_features_multiple_image_pairs():
    image_names = "none"
    for image_name in image_names:
        test_finding_features_image_pair(image_name)


def test_warping_errors():
    # TODO: find matches using two methods and wrap the image (compute homography?)
    # Or another method used in the demo
    return None


def test_wide_feld_of_view_warping_errors():
    # TODO: do the same thing as test_warping_errors, except for wide field of view cameras
    return None


def main():
    image1_name = '../test_frames/1021700006.jpeg'
    image2_name = '../test_frames/1021700005.jpeg'
    test_finding_features_image_pair([image1_name, image2_name])


if __name__ == "__main__":
    main()

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


# TODO: 1. Make a warp to see the errors
#       2. Evaluate the performance on wide field of view camera
#       3. when features not found, load the referencer pto matches
#       4. Spherical warper testing: detail::SphericalWarper

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
    matches, cam1_pts, cam2_pts = hugin_api.hugin_find_matches(image_names)
    # TODO: keyponts should be opencv KeyPoints Object
    cam1_pts = toKeyPoints(cam1_pts)
    cam2_pts = toKeyPoints(cam2_pts)
    # TODO: implement these methods 
    matching_visualizer.visualize(matches, image1, image2, cam1_pts, cam2_pts)


def test_finding_features_multiple_image_pairs():
    image_names = "none"
    for image_name in image_names:
        test_finding_features_image_pair(image_name)


def main():
    image1_name = '../test_frames/1021700006.jpeg'
    image2_name = '../test_frames/1021700005.jpeg'
    test_finding_features_image_pair([image1_name, image2_name])


if __name__ == "__main__":
    main()

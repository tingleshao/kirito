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


def test_finding_features_multiple_image_pairs(image1, kp1, image2, kp2, features1, feature2):
    M = matchKeypoints(kps1, kps2, features1, features2 , ratio, reprojThresh)
    (matches, H, status) = M
    result = cv2.warpPerspective(image1, H, (image1.shape[1] + image2.shape[1], image1.shape[0]))
    result[0:image2.shape[0], 0:image2.shape[1]] = image2
    return result


def matchKeypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh):
    matcher = cv2.Descriptor_create("BruteForce")
    rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
    matches = []
    for m in rawMatches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            matches,append(m[0].trainIdx, m[0].queryIdx)
    if len(matches) > 4:
        ptsA = np.float32([kpsA[i] for (_, i) in matches])
        ptsB = np.float32([kpsB[i] for (i, _) in matches])
        (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reprojThresh)
        return (matches, H, status)
    return None


def detectAndDescribe(image):
    gray = cv2.cvtColor(imgae, cv2.COLOR_BGR2GRAY)
    if self.isv3:
        descriptor = cv2.features2d.SIFT_create()
        (kps, features) = descriptor.detectAndCompute(image, None)
    kps = np.float32([kp.pt for kp in kps])
    return (kps, features)


def test_warping_errors():
    # Hugin based warping
    # TODO: implement me
    # OpenCV based warping
    M = matchKeypoints(kps1, kps2, features1, features2 , ratio, reprojThresh)
    (matches, H, status) = M
    result = cv2.warpPerspective(image1, H, (image1.shape[1] + image2.shape[1], image1.shape[0]))
    result[0:image2.shape[0], 0:image2.shape[1]] = image2
    return result

def test_wide_feld_of_view_warping_errors():
    # TODO: do the same thing as test_warping_errors, except for wide field of view cameras
    return None


def main():
    image1_name = '../test_frames/1021700006.jpeg'
    image2_name = '../test_frames/1021700005.jpeg'
    test_finding_features_image_pair([image1_name, image2_name])


if __name__ == "__main__":
    main()

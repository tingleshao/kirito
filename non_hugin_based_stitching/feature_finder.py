import cv2
import os
import sys
from numpy.misc import imread, imsave


def main():
    features = sys.argv[1]
    match_conf = sys.argv[2]
    range_width = sys.argv[3]
    conf_thresh = sys.argv[4]
    orb = cv2.ORB_create()
    image_names = # XXX:
    imgs = []
    seam_scale = # XXX:
    # prepare all images
    for image_name in image_names:
        full_img = imread(image_name)
        img_size = full_img.shape
        rows = img_size[0]
        cols = img_size[1]
        imgs.append(imresize(full_img, [rows, cols] * seam_scale))
        # find features
        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)
            

if __name__ == "__main__":
    main()

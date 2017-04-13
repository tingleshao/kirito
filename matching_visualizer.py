# visualize matches

# input parameter:
# python matching_visualizer.py img1_id img2_id
#
# display the features with circles and indices in two images
import sys
import cv2
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



def main():




    return None

def visualize(img1_name, feature1, img2_name, feature2):
    # feature locations are expected to be scaled and ordered
    #
    img1 = Image.open(img1_name)
    img2 = Image.open(img2_name)


    cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches1to2[, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]]) → outImg


if __name__ == "__main__":
    main()

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


    
def visualize(img1_name, match1, img2_name, match2):
    # feature locations are expected to be scaled and ordered
    img1 = Image.open(img1_name)
    img2 = Image.open(img2_name)
    draw1 = ImageDraw.draw(img1)
    draw2 = ImageDraw.draw(img2)
    num_of_matches = len(match1)
    r = 5
    font = ImageFont.truetype("sans-serif.ttf", 16)
    for i in range(num_of_matches):
        x1 = match1[i][0]
        y1 = match1[i][1]
        x2 = match2[i][0]
        y2 = match2[i][1]
        draw1.ellipse((x1-r, y1-r, x1+r, y1+r), fill=(255,0,0,0))
        draw2.ellipse((x2-r, y2-r, x2+r, y2+r), fill=(255,0,0,0))
        draw1.text((x1, y1), str(i), (255,255,255),font=font)
        draw2.text((x2, y2), str(i), (255,255,255),font=font)
    img1.save("annonated" + img1_name)
    img2.save("annonated" + img2_name)
    #cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches1to2[, outImg[, matchColor[, singlePointColor[, matchesMask[, flags]]]]]) → outImg


if __name__ == "__main__":
    main()

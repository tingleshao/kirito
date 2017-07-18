# visualize matches

# input parameter:
# python matching_visualizer.py img1_id img2_id
#
# display the features with circles and indices in two images
import sys
import cv2
from PIL import Image
from PIL import ImageFont
import matplotlib.pyplot as plt
from PIL import ImageDraw


def main():
    img1_name = "test_frames/1021700000.jpeg"
    img2_name = "test_frames/1021700002.jpeg"
    orb = cv2.ORB()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    visualize(img1_name, kp1, img2_name, kp2)


def visualize(img1_name, match1, img2_name, match2):
    # feature locations are expected to be scaled and ordered
    img1 = Image.open(img1_name)
    img2 = Image.open(img2_name)
    draw1 = ImageDraw.Draw(img1)
    draw2 = ImageDraw.Draw(img2)
    num_of_matches = len(match1)
    r = 5
    font = ImageFont.truetype("Skia.ttf", 16)
    for i in range(num_of_matches):
        x1 = match1[i][0]
        y1 = match1[i][1]
        x2 = match2[i][0]
        y2 = match2[i][1]
        draw1.ellipse((x1-r, y1-r, x1+r, y1+r), fill=(255,0,0,0))
        draw2.ellipse((x2-r, y2-r, x2+r, y2+r), fill=(255,0,0,0))
        draw1.text((x1, y1), str(i), (255,255,255), font=font)
        draw2.text((x2, y2), str(i), (255,255,255), font=font)
    img1.save("annonated" + img1_name)
    img2.save("annonated" + img2_name)


def visualize(matches, img1, img2, kp1, kp2):
    draw_params = dict(matchColor = (0, 255, 0),
                       singlePointColor = (255, 0 ,0),
                       flags = 0)
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
    plt.figure()
    plt.imshow(img3,),plt.draw()


def visualize_result(result):
    plt.figure()
    plt.imshow(result), plt.draw()


def visualize_features_from_pto_files(pto_file_name, camera1_id, camera2_id):
    with open(pto_file_name, 'r') as pto_file:
        pto_str = pto_file.read()
    pto_str_lines = pto_str.split('\n')
    display_lst = []
    camera_count = 0
    camera1_filename = ""
    camera2_filename = ""
    for line in pto_str_lines:
        if len(line) > 0 and line[0] == "i":
            camera_count += 1
            if camera_count == camera1_id:
                tokens = line.split(" ")
                camera1_filename = tokens[-1][1:]
            if camera_count == camera2_id:
                tokens = line.split(" ")
                camera2_filename = tokens[-1][1:]
        if len(line) > 0 and line[0] == "c":
            tokens = line.split(" ")
            cam1_id = int(tokens[1][1:])
            cam2_id = int(tokens[2][1:])
            if cam1_id == camera1_id and cam2_id == camera2_id:
                display_lst.append(line)
    # convert the display_lst into matches, kps and images
    camera1_image = cv2.imread(camera1_filename)
    camera2_image = cv2.imread(camera2_filename)
    idx = 0
    cam1_ptx = []
    cam2_pts = []
    for line in display_lst:
        tokens = line.split(" ")
        cam1_x = float(tokens[3][1:])
        cam1_y = float(tokens[4][1:])
        cam1_pts.append((cam1_x, cam1_y))
        cam2_x = float(tokens[5][1:])
        cam2_y = float(tokens[6][1:])
        cam2_pts.append((cam2_x, cam2_y))
        dmatch = cv2.DMatch(idx, idx, 0)
        matches.append([dmatch])
    kp1 = hugin_api.toKeyPoints(cam1_pts)
    kp2 = hugin_api.toKeyPoints(cam2_pts)
    matching_visualizer.visualize(matches, camera1_image, camera2_image, kp1, kp2)


if __name__ == "__main__":
    main()

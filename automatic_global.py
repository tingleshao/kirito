from subprocess import call
import cv2
import os


# down scale the local vie images so that hugin can find the features (perhaps)
# input image dimension: 3840 x 2160
localview_img = cv2.imread("10.0.1.1_sensor1.jpg")
scaled_localview = cv2.resize(localview_img, (693, 390))
cv2.imwrite('10.0.1.1_sensor1_scaled.jpg', scaled_localview)

# generating project file
os.system("pto_gen -o init.pto 10.0.1.7_sensor1.jpg 10.0.1.1_sensor1_scaled.jpg")

# generating control points
os.system("cpfind --multirow -o control_pts.pto init.pto")

# pruning control points
os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")

# optimizing positions and geometry
os.system("autooptimiser -a -l -s -m -o optimized.pto pruning_pts.pto");

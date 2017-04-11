import os
import sys
# This script does the similar thing as automatic_with_opencv.py, but includes the global view image in the stitching.
# process:
# 1. read in the images,
# 2. find features in all images, including the global one
# 3. filter out matches, only leave matches between small view and global view
# 4. run model estimation

enhance_image = False
use_ip_files = True
clean_up = False

# this map is different than the one in the other script: it contians the global view
# global view has id 0
#sensor_id_map = [(1, 1, 17), (1, 2, 16), (2, 1, 15), (3, 1, 14), (4, 1, 13), (4, 2, 12), (5, 1, 4), (5, 2, 3), (2, 2, 2), (3, 2, 1),
#                 (8, 1, 0), (8, 2, 11), (9, 1, 5), (9, 2, 6), (6, 1, 7), (6, 2, 8), (10, 1, 9), (10, 2, 10), (7, 1, 0)]
sensor_id_map = [(1, 1, 5), (1, 2, 6), (2, 1, 7), (3, 1, 9), (4, 1, 4), (4, 2, 3), (5, 1, 2), (5, 2, 1),
                 (2, 2, 8), (3, 2, 10), (8, 1, 15), (8, 2, 14), (9, 1, 13), (9, 2, 12), (6, 1, 0),
                 (6, 2, 11), (7, 1, 17), (7, 2, 16), (10, 1, -1)]

if use_ip_files:
    os.system("mkdir old_order_images")
    os.system("mv *.jpg old_order_images")
    for item in sensor_id_map:
        ip = int(item[0]/1)
        sensor_id = int(item[1])
        old_id = item[2]
        os.system("cp old_order_images/10.0.2.{0}_sensor{1}.jpg mcam_{2}_scale_2.jpg".format(ip, sensor_id, old_id+1))
        if enhance_image:
            img = cv2.imread("mcam_{0}_scale_2.jpg".format(old_id+1))
            new_img = cv2.resize(img, (1228, 920))
            enhanced_img = enhance(new_img)
            cv2.imwrite("mcam_{0}_scale_2.jpg".format(old_id+1), new_img)


# call the opencv customized
os.system("./feature_finder mcam_0_scale_2.jpg mcam_1_scale_2.jpg mcam_2_scale_2.jpg mcam_3_scale_2.jpg mcam_4_scale_2.jpg mcam_5_scale_2.jpg mcam_6_scale_2.jpg mcam_7_scale_2.jpg mcam_8_scale_2.jpg mcam_9_scale_2.jpg mcam_10_scale_2.jpg  mcam_11_scale_2.jpg mcam_12_scale_2.jpg mcam_13_scale_2.jpg mcam_14_scale_2.jpg mcam_15_scale_2.jpg mcam_16_scale_2.jpg mcam_17_scale_2.jpg mcam_18_scale_2.jpg --features orb --match_conf " + sys.argv[1] + " --rangewidth 8 --conf_thresh 0.5 | tee feature_finder_output.txt")

# convert the output into a simplified format
os.system("python3 parse_opencv_output.py feature_finder_output.txt")

# remove the false matches by limiting the features to be found on global view
os.system("python3 filter_features_based_on_global_view.py")

# remove the false matches by limiting the pixel coordinates to be the overlapping regions
os.system("python3 filter_features_based_on_locations.py")

# convert the simplified output to hugin format
os.system("python3 parse_output_for_hugin.py")

# put all the parts togethero generate the pto file
os.system("python3 generate_hugin_input.py")

# use hugin tools to filter features, and genrate paranoma
os.system("celeste_standalone -i test0.pto -o pruning_pts.pto")

os.system("cpclean -o pruning_pts2.pto pruning_pts.pto")

os.system("autooptimiser -a -l -s -m -o optimized.pto pruning_pts2.pto")

if clean_up:
    os.system("rm *.txt")
    os.system("mv optimzied.pto optimized")
    os.system("rm *.pto")
    os.system("mv optimized optimized.pto")

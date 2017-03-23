from subprocess import call
import os
import cv2


def enhance(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return img_output

rename_files = False
use_ip_files = True
clean_up = False

sensor_id_map = [(1, 1, 17), (1, 2, 16), (2, 1, 15), (3, 1, 14), (4, 1, 13), (4, 2, 12), (5, 1, 4), (5, 2, 3), (2, 2, 2), (3, 2, 1), (8, 1, 0), (8, 2, 11),
                 (9, 1, 5), (9, 2, 6), (6, 1, 7), (6, 2, 8), (10, 1, 9), (10, 2, 10)]

if rename_files:
    os.system("mkdir old_order_images")
    os.system("mv mcam*.jpg old_order_images")
    os.system("cp old_order_images/mcam_1_scale_2.jpg mcam_13_scale_2.jpg")
    os.system("cp old_order_images/mcam_2_scale_2.jpg mcam_14_scale_2.jpg")
    os.system("cp old_order_images/mcam_3_scale_2.jpg mcam_15_scale_2.jpg")
    os.system("cp old_order_images/mcam_4_scale_2.jpg mcam_16_scale_2.jpg")
    os.system("cp old_order_images/mcam_5_scale_2.jpg mcam_17_scale_2.jpg")
    os.system("cp old_order_images/mcam_6_scale_2.jpg mcam_18_scale_2.jpg")
    os.system("cp old_order_images/mcam_7_scale_2.jpg mcam_12_scale_2.jpg")
    os.system("cp old_order_images/mcam_8_scale_2.jpg mcam_1_scale_2.jpg")
    os.system("cp old_order_images/mcam_9_scale_2.jpg mcam_2_scale_2.jpg")
    os.system("cp old_order_images/mcam_10_scale_2.jpg mcam_3_scale_2.jpg")
    os.system("cp old_order_images/mcam_11_scale_2.jpg mcam_4_scale_2.jpg")
    os.system("cp old_order_images/mcam_12_scale_2.jpg mcam_5_scale_2.jpg")
    os.system("cp old_order_images/mcam_13_scale_2.jpg mcam_11_scale_2.jpg")
    os.system("cp old_order_images/mcam_14_scale_2.jpg mcam_10_scale_2.jpg")
    os.system("cp old_order_images/mcam_15_scale_2.jpg mcam_9_scale_2.jpg")
    os.system("cp old_order_images/mcam_16_scale_2.jpg mcam_8_scale_2.jpg")
    os.system("cp old_order_images/mcam_17_scale_2.jpg mcam_7_scale_2.jpg")
    os.system("cp old_order_images/mcam_18_scale_2.jpg mcam_6_scale_2.jpg")

if use_ip_files:
    os.system("mkdir old_order_images")
    os.system("mv *.jpg old_order_images")
    for item in sensor_id_map:
        ip = int(item[0] / 1)
        sensor_id = int(item[1])
        old_id = item[2]
        os.system("cp old_order_images/10.0.1.{0}_sensor{1}.jpg mcam_{2}_scale_2.jpg".format(ip, sensor_id, old_id+1))
    #    img = cv2.imread("mcam_{0}_scale_2.jpg".format(old_id+1))
    #    new_img = cv2.resize(img, (1228, 920))
    #    enhanced_img = enhance(new_img)
        #cv2.imwrite("mcam_{0}_scale_2.jpg".format(old_id+1), new_img)


# call the opencv customzied
#if not use_ip_files:
os.system("./feature_finder mcam_1_scale_2.jpg mcam_2_scale_2.jpg mcam_3_scale_2.jpg mcam_4_scale_2.jpg mcam_5_scale_2.jpg mcam_6_scale_2.jpg mcam_7_scale_2.jpg mcam_8_scale_2.jpg mcam_9_scale_2.jpg mcam_10_scale_2.jpg  mcam_11_scale_2.jpg mcam_12_scale_2.jpg mcam_13_scale_2.jpg mcam_14_scale_2.jpg mcam_15_scale_2.jpg mcam_16_scale_2.jpg mcam_17_scale_2.jpg mcam_18_scale_2.jpg --features orb --match_conf 0.3 | tee sample_output_0.txt")
#else:
#    os.system("foo")

# convert the output into a simplified format
os.system("python3 parse_opencv_output.py sample_output_0.txt")

# convert the simplified output to hugin format
os.system("python3 parse_output_for_hugin.py")

# put all the parts together to generate the pto file
os.system("python3 generate_hugin_input.py")

# use hugin tools to filter features, and generate paranoma
os.system("celeste_standalone -i test0.pto -o pruning_pts.pto")

os.system("cpclean -o pruning_pts2.pto pruning_pts.pto")

os.system("autooptimiser -a -l -s -m -o optimized.pto pruning_pts2.pto");

if clean_up:
    os.system("rm *.txt")
    os.system("mv optimized.pto optimized")
    os.system("rm *.pto")
    os.system("mv optimized optimized.pto")

from subprocess import call
import os


rename_files = False

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

# call the opencv customzied
os.system("./feature_finder mcam_1_scale_2.jpg mcam_2_scale_2.jpg mcam_3_scale_2.jpg mcam_4_scale_2.jpg mcam_5_scale_2.jpg mcam_6_scale_2.jpg mcam_7_scale_2.jpg mcam_8_scale_2.jpg mcam_9_scale_2.jpg mcam_10_scale_2.jpg  mcam_11_scale_2.jpg mcam_12_scale_2.jpg mcam_13_scale_2.jpg mcam_14_scale_2.jpg mcam_15_scale_2.jpg mcam_16_scale_2.jpg mcam_17_scale_2.jpg mcam_18_scale_2.jpg --features orb | tee sample_output_0.txt")

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

# TODO: optional: clean up, remove intmediate files

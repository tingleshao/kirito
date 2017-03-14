from subprocess import call

import os

# TODO: rename the image files

# call the opencv customzied
os.system("./stitching_detailed2 mcam_1_scale_2.jpg mcam_2_scale_2.jpg mcam_3_scale_2.jpg mcam_4_scale_2.jpg mcam_5_scale_2.jpg mcam_6_scale_2.jpg mcam_7_scale_2.jpg mcam_8_scale_2.jpg mcam_9_scale_2.jpg mcam_10_scale_2.jpg  mcam_11_scale_2.jpg mcam_12_scale_2.jpg mcam_13_scale_2.jpg mcam_14_scale_2.jpg mcam_15_scale_2.jpg mcam_16_scale_2.jpg mcam_17_scale_2.jpg mcam_18_scale_2.jpg --features orb --ba reproj > sample_output_0.txt")

# convert the output into a simplified format
os.system("python3 parse_opencv_output.py sample_output_0.txt")

# convert the simplified output to hugin format
# TODO: process the hugin format file to remove some matches

os.system("python3 parse_output_for_hugin.py")



# put all the parts together to generate the pto file
os.system("python3 generate_hugin_input.py")

# TODO: hugin filter features



# TODO: optional: clean up, remove intmediate files

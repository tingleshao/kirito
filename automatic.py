from subprocess import call
import sys
import os


stage = sys.argv[1]
# generating project file
if stage == '0':
    os.system("pto_gen -f 14.4 -o init.pto mcam_1_scale_2.jpg mcam_2_scale_2.jpg mcam_3_scale_2.jpg mcam_4_scale_2.jpg mcam_5_scale_2.jpg mcam_6_scale_2.jpg mcam_7_scale_2.jpg mcam_8_scale_2.jpg mcam_9_scale_2.jpg mcam_10_scale_2.jpg  mcam_11_scale_2.jpg mcam_12_scale_2.jpg mcam_13_scale_2.jpg mcam_14_scale_2.jpg mcam_15_scale_2.jpg mcam_16_scale_2.jpg mcam_17_scale_2.jpg mcam_18_scale_2.jpg")

elif stage == '1':
# generating control points
    os.system("cpfind --multirow -o control_pts.pto init.pto")

# pruning control points
    os.system("cpclean -o  control_pts2.pto control_pts.pto")

    os.system("celeste_standalone -i control_pts2.pto -o pruning_pts.pto")

    os.system("linefind -o lines.pto pruning_pts.pto")

# optimizing positions and geometry
    os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");

    os.system("hugin_executor --stitching --prefix=prefix optimized.pto")

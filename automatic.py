from subprocess import call
import sys
import os


# call snap to take images
if len(sys.argv) > 1 and argv[1] == "snap":
    os.system("snap -c sync.cfg")

# generating project file
os.system("pto_gen -f 14.4 -o init.pto *.jpg")

#os.system("python3 update_crop_factor.py init.pto")
# generating control points
#os.system("cpfind --multirow -o control_pts.pto init2.pto")

# pruning control points
#os.system("cpclean -o control_pts2.pto control_pts.pto")

#os.system("celeste_standalone -i control_pts2.pto -o pruning_pts.pto")

#os.system("linefind -o lines.pto pruning_pts.pto")

# optimizing positions and geometry
#os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");

#os.system("python3 HuginMakeSaccadeConfig.py optimized.pto model.json")
    #os.system("hugin_executor --stitching --prefix=prefix optimized.pto")

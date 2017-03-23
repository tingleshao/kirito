from subprocess import call

import os

# TODO: rename the image files


# generating project file
os.system("pto_gen -o init.pto *.jpg")

# generating control points
os.system("cpfind --multirow -o control_pts.pto init.pto")

# pruning control points
os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")

# optimizing positions and geometry
os.system("autooptimiser -a -l -s -m -o optimized.pto pruning_pts.pto");

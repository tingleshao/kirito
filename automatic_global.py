from subprocess import call

import os


# generating project file
os.system("pto_gen -o init.pto 10.0.1.7_sensor1.jpg 10.0.1.1_sensor1.jpg")

# generating control points
os.system("cpfind --multirow -o control_pts.pto init.pto")

# pruning control points
os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")

# optimizing positions and geometry
os.system("autooptimiser -a -l -s -m -o optimized.pto pruning_pts.pto");

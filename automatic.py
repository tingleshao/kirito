from subprocess import call
import sys
import os
import kgui.main as gui


# Color coded output helps visualize the information a little better, plus looks cool!
class ansi:
    BOLD = '\033[1;97m'
    WHITE = '\033[0;97m'
    YELLOW = '\033[0;33m'
    YELLOW_B = '\033[0;33m'
    RED = '\033[0;31m'
    RED_B = '\033[1;31m'
    BLUE = '\033[0;94m'
    BLUE_B = '\033[1;94m'
    CYAN = '\033[0;36m'
    CYAN_B = '\033[1;36m'
    ENDC = '\033[0m'

# TODO: update readme to mention QT dependency

# call snap to take images
if len(sys.argv) > 1 and sys.argv[1] == "snap":
    os.system("snap -c sync.cfg")

if len(sys.argv) > 1 and sys.argv[1] == "gui":
    string = "\n{}Launching GUI\n"
    print(string.format(ansi.RED_B))
    gui.main()

# generating project file
#os.system("pto_gen -f 14.4 -o init.pto *.jpg")

#os.system("python3 update_crop_factor.py init.pto")
# generating control points
os.system("cpfind --prealigned --kdtreeseconddist=0.45 -o control_pts.pto init2.pto")

# pruning control points
#os.system("cpclean -o control_pts2.pto control_pts.pto")

os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")

os.system("linefind -o lines.pto pruning_pts.pto")

# optimizing positions and geometry
os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto")

#os.system("python3 HuginMakeSaccadeConfig.py optimized.pto model.json")
    #os.system("hugin_executor --stitching --prefix=prefix optimized.pto")

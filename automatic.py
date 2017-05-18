import os
import sys

import kgui.main as gui
import stitching


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

# call snap to take images
if len(sys.argv) > 1 and sys.argv[1] == "snap":
    os.system("snap -c sync.cfg")

if len(sys.argv) > 1 and sys.argv[1] == "gui":
    string = "\n{}Launching GUI\n"
    print(string.format(ansi.RED_B))
    gui.main()

stitching.stitching_pure_hugin()

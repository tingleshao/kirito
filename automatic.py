import os
import sys

import kgui.main as gui
import stitching

import argparse

# Arguments
parser = argparse.ArgumentParser(description="",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
add_arg = parser.add_argument

add_arg('--gui', action='store_true', help="Launch the GUI.")
add_arg('--test', action="store_true", help="Run in test mode (not acturally grabbing images from a Mantis Camera).")


args = parser.parse_args()

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

if args.gui:
    string = "\n{}Launching GUI\n"
    print(string.format(ansi.RED_B))
    gui.main(test=True)

if args.test:
    stitching.stitching_pure_hugin()

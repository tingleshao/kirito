# update the code from applications:stitching_gui
import os
from sys import platform
 

if platform == "darwin":
    applications_dir = '/Users/chongshao/dev/applications/stitching_app'
if platform == "linux":
    applications_dir = "/home/cshao/dev/applications/stitching_app"

os.system("cp {0}/*.py .".format(applications_dir))
os.system("cp {0}/utils/*.py utils/".format(applications_dir))
os.system("cp {0}/rendering/*.py rendering/".format(applications_dir))
os.system("cp {0}/non_hugin_based_stitching/*.py non_hugin_based_stitching/".format(applications_dir))
os.system("cp {0}/kgui/*.py kgui/".format(applications_dir))
os.system("cp {0}/grab_tools/*.py grab_tools/".format(applications_dir))
os.system("cp {0}/hugin_api/*.py hugin_api/".format(applications_dir))

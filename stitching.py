import datetime
import getpass
import os
import time


def stitching_pure_hugin(threshold, working_dir, max_visible_scale, radial):
    print("stitching button clicked!")
    cwd = os.getcwd()
    os.chdir(working_dir)
    os.system("cpfind --prealigned --kdtreeseconddist=" + str(float(threshold)/100) + " -o control_pts.pto prealigned.pto")
    # pruning control points
    os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")
    os.system("linefind -o lines.pto pruning_pts.pto")
    # optimizing positions and geometry
    os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");
    os.system("pano_modify -o optimized_centered.pto --center --straighten --canvas=AUTO optimized.pto")
    os.system("python3 {0}/update_pto_resolution.py".format(cwd))
    #os.system("hugin_executor --stitching optimized_s.pto")
    os.system("nona -m JPEG -v -z 85 -o preview.jpg optimized_s.pto")
    os.system('convert preview.jpg -resize 608x421 preview.jpg')
#    os.system('convert *.tif" preview.jpg')
    os.system("cp {0}/reference.json .".format(cwd))
    os.system("python3 {0}/HuginMakeSaccadeConfig.py optimized.pto model.json ".format(cwd) + max_visible_scale + " " + radial)
    os.chdir(cwd)


def stitching_pure_hugin_without_existing_model(threshold, working_dir, max_visible_scale, radial):
    print("stitching button clicked!")
    # save the current working path
    cwd = os.getcwd()
    # change the current working path
    os.chdir(working_dir)
    print("current dir: " + os.getcwd())
    os.system("pto_gen *.jpeg -o init.pto")
    os.system("cpfind --multirow -o control_pts.pto init.pto")
    # pruning control points
    os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")
    os.system("linefind -o lines.pto pruning_pts.pto")
    # optimizing positions and geometry
    os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");
    os.system("pano_modify -o optimized_centered.pto --center --straighten --canvas=AUTO optimized.pto")
    os.system("python3 {0}/update_pto_resolution.py".format(cwd))
    #os.system("hugin_executor --stitching optimized_s.pto")
    os.system("nona -m JPEG -v -z 85 --ignore-exposure -o preview.jpg optimized_s.pto ")
    os.system('convert preview.jpg -resize 608x421 preview.jpg')
    #os.system('convert "*.tif" -resize 608x421 preview.jpg')
    os.system("cp {0}/reference.json .".format(cwd))
    os.system("python3 {0}/HuginMakeSaccadeConfig.py optimized.pto model.json ".format(cwd) + max_visible_scale + " " + radial)
    # change back to the current working path
    os.chdir(cwd)


def prepare_directory():
    username = getpass.getuser()
    if not os.path.exists("/home/" + username + "/data"):
        os.system("mkdir " + "/home/" + username + "/data")
    if not os.path.exists("/home/" + username + "/data/stitching"):
        os.system("mkdir " + "/home/" + username + "/data/stitching")
    dt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    os.system("mkdir /home/" + username + "/data/stitching/" + dt)
    return "/home/" + username + "/data/stitching/" + dt


def preview_hugin():
    if not("preview.jpg" in os.listdir()):
        os.system("nona -m JPEG -v -z 85 --ignore-exposure -o preview.jpg optimized_s.pto")
        os.system('convert preview.jpg -resize 608x421 preview.jpg')

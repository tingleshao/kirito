import datetime
import getpass
import os
import time
import subprocess
import json
import utils.utils as utils


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
    utils.update_pto_resolution()
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
    utils.update_crop_factor("init.pto")
    os.system("cpfind --multirow -o control_pts.pto init2.pto")
    # pruning control points
    os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")
    os.system("linefind -o lines.pto pruning_pts.pto")
    # optimizing positions and geometry
    os.system("autooptimiser -a -l -s -m -o optimized.pto lines.pto");
    os.system("pano_modify -o optimized_centered.pto --center --straighten --canvas=AUTO optimized.pto")
    utils.update_pto_resolution()
    #os.system("hugin_executor --stitching optimized_s.pto")
    os.system("nona -m JPEG -v -z 85 -o preview.jpg optimized_s.pto ")
    os.system('convert preview.jpg -resize 608x421 preview.jpg')
    #os.system('convert "*.tif" -resize 608x421 preview.jpg')
    os.system("cp {0}/reference.json .".format(cwd))
    os.system("python3 {0}/HuginMakeSaccadeConfig.py optimized.pto model.json ".format(cwd) + max_visible_scale + " " + radial)
    # change back to the current working path
    os.chdir(cwd)


# prepare directory always has the date after the input dir
def prepare_directory(default_dir):
    if not os.path.exists(default_dir):
        os.system("mkdir " + default_dir)
    dt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    os.system("mkdir " + default_dir + "/" + dt)
    return default_dir + "/" + dt


def preview_hugin(work_dir):
    cwd = os.getcwd()
    os.chdir(work_dir)
    if not("preview.jpg" in os.listdir()):
        os.system("nona -m JPEG -v -z 85 --ignore-exposure -o preview.jpg optimized_s.pto")
        os.system('convert preview.jpg -resize 608x421 preview.jpg')
    os.chdir(cwd)


def check_updated_pto_file(working_dir):
    # check the last changed pto file
    # find the recently changed pto files
    cwd = os.getcwd()
    # change the current working path
    os.chdir(working_dir)
    a = subprocess.check_output("find -cmin -100 -printf \"%T+\\t%p\\n\" | sort", shell=True)
    c = [b.split("\\t")[1] for b in str(a).split("\\n") if len(b.split("\\t")) > 1 and len(b.split("\\t")[1]) > 4]
#    changed_files = os.system("find -cmin -100 -printf \"%T+\\t%p\\n\" | sort").split("\n")
    print(c)
    if len(c) > 0:
       pto_file_name = c[-1]
    else:
       return
    os.chdir(cwd)
    # remove the "./" in file name
    return pto_file_name[2:]


def update_saved_reference_pto_file_location(location):
    config_file_location = "./reference_pto_file_location.json"
    data = {"pto_file_location" : location}
    with open('reference_pto_file_location.json', 'w') as f:
         json.dump(data, f, ensure_ascii=False)

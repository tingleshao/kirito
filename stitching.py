import datetime
import getpass
import os
import time
import subprocess
import json
import utils.utils as utils
import numpy as np
from matplotlib import pyplot as plt
import cv2
from scipy import misc
import glob


# TODO: test
# TODO: may adding a switch for add/NOT features from referece pto
def stitching_pure_hugin(threshold, working_dir, max_visible_scale, radial):
    print("stitching button clicked!")
    cwd = os.getcwd()
    os.chdir(working_dir)
    os.system("cpfind --prealigned --kdtreeseconddist=" + str(float(threshold)/100) + " -o control_pts.pto prealigned.pto")
    # pruning control points
    os.system("celeste_standalone -i control_pts.pto -o pruning_pts.pto")
    empty_feature_cam_ids = check_number_of_features_for_every_camera("pruning_pts.pto")
    # append pto feautres from reference pto to pruning_pts pto
    copy_reference_features_to_current_pto("prealigned.pto", "pruning_pts.pto", empty_feature_cam_ids)
    os.system("linefind -o lines.pto pruning_pts_adding_feature.pto")
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


def match_color(model_dir, image_dir):
    import mantisStitchingFunctions as msf ##### Must have mantisStitchingFunctions.py in path
    N_desired_slots = np.size(desired_slots);
    #image_extension='tiff';
    image_extension='.jpeg';
    # Specify the gamma and max possible pixel value
    g = 2.4
    max_I = 2**8-1
    down_sample_factor = 3
    iterations = 2
    # Load the JSON file
    with open(json_dir+'model.json', 'r') as data_file:
        calibration = json.loads(data_file.read())
    # Load data from JSON
    N_slots = np.size(calibration['camera_stitch_params']['microcameras'])
    F = np.zeros(N_desired_slots,dtype=np.double())
    Slot = np.zeros(N_desired_slots,dtype=np.double())
    K1 = np.zeros(N_desired_slots,dtype=np.double())
    Yaw =np.zeros(N_desired_slots,dtype=np.double())
    Pitch = np.zeros(N_desired_slots,dtype=np.double())
    Roll = np.zeros(N_desired_slots,dtype=np.double())
    gain = np.zeros(N_desired_slots,dtype=np.double())
    # Read params from the JSON object
    for n in range(0,N_desired_slots):
        for m in range(0,N_slots):
            Slot_m = calibration['camera_stitch_params']['microcameras'][m]['Slot']
            if desired_slots[n] == Slot_m:
                Slot[n] = Slot_m
                F[n] = calibration['camera_stitch_params']['microcameras'][m]['F']
                K1[n] = calibration['camera_stitch_params']['microcameras'][m]['K1']
                Yaw[n] = calibration['camera_stitch_params']['microcameras'][m]['Yaw']
                Pitch[n] = calibration['camera_stitch_params']['microcameras'][m]['Pitch']
                Roll[n] = calibration['camera_stitch_params']['microcameras'][m]['Roll']
                gain[n] = calibration['camera_stitch_params']['microcameras'][m]['gain']
    # Adjust params by downsample factor
    F = F/down_sample_factor
    # Determine required M to match pixel sizes
    average_F = np.mean(F)
    M = F/average_F
    pixel_size = (180/np.pi)*(1/average_F)
    Nx = calibration['camera_stitch_params']['global']['sensorwidth']
    Ny = calibration['camera_stitch_params']['global']['sensorheight']

    Nx_ds = np.ceil(Nx/down_sample_factor)
    Ny_ds = np.ceil(Ny/down_sample_factor)
    image_width = pixel_size*Nx_ds
    image_height = pixel_size*Ny_ds

    # Normalize Yaw and Pitch and determine offsets
    Yaw = Yaw - np.min(Yaw)
    Pitch = np.max(Pitch) - Pitch
    offset_x = np.floor(Yaw/pixel_size)
    subshift_x = Yaw/pixel_size - offset_x
    offset_y = np.floor(Pitch/pixel_size)
    subshift_y = Pitch/pixel_size - offset_y
    N_rows = np.max(offset_y)+Ny
    N_cols = np.max(offset_x)+Nx
    image_names = glob.glob(image_dir+'*'+image_extension)
    better = np.zeros(N_desired_slots)
    #Now load the images
    for i in range(0,N_desired_slots):
        print(i)
        image_names[i] = (glob.glob(image_dir+'*_'+str(int(Slot[i]))+image_extension))[0]
    N_files = np.size(image_names)
    for n in range(0,N_desired_slots):
        #for m in range(0,N_slots):
        for m in range(0,max(desired_slots)+1):
            if desired_slots[n] == m:
                temp = cv2.imread(image_names[n][:], cv2.IMREAD_UNCHANGED)
                fov_temp = np.uint8(temp[:,:,1]!=0)
                #fov_temp[:,:]=1
                fov_temp[:,:]=np.uint8(pow(2,8)-1)
                temp = cv2.imread(image_names[n][:])
                temp = cv2.cvtColor(temp, cv2.COLOR_BGR2RGB)
                #Downsample the image
                dsf = np.int(np.floor(1/np.double(down_sample_factor)*100))
                image_temp = misc.imresize(temp, dsf,interp='bilinear' )
                if n == 0:
                    image_data = np.zeros([np.size(image_temp[:,1,1]),np.size(image_temp[1,:,1]),3,N_desired_slots],dtype=np.double())
                    fov_frame = np.zeros([np.size(image_temp[:,1,1]),np.size(image_temp[1,:,1]),N_desired_slots],dtype=np.double())
                Nr = np.size(fov_temp[:,0]);
                Nc = np.size(fov_temp[0,:]);
                a  = 2/np.sqrt(Nr^2 + Nc^2);
                x  = (a*Nc/2)*np.linspace(-1, 1, Nc);
                y  = (a*Nr/2)*np.linspace(-1, 1, Nr);
                x2, y2 = np.meshgrid(x,y);
                r, theta = msf.cart2pol(x2,y2)
                fov_R = 0.98*((np.max(x2*np.double(fov_temp))) - np.min(x2*np.double(fov_temp)))/2
                fov_temp = np.uint8( misc.imresize(fov_temp, dsf,interp='bilinear' ))
                #Remove the lens distortion
                print("Removing Lens distortion")
                image_temp = msf.distortImage(image_temp, K1[n])
                fov_temp = msf.distortImage(fov_temp, K1[n])
                #Apply the Mcam magifnication
                print("Magnifiying Image")
                image_temp = msf.MagnifyImage(image_temp,1/M[n])
                fov_temp = msf.MagnifyImage(fov_temp,1/M[n])
                #adjust for camera Roll
                print("Adjusting Roll")
                image_temp = misc.imrotate(image_temp, -Roll[n], interp='bilinear')
                fov_temp = misc.imrotate(fov_temp, -Roll[n], interp='bilinear')
                #Adujust subpixel alignment
                print("Applying Shift")
                image_temp = msf.ShiftImage(image_temp, subshift_y[n], subshift_x[n]);
                fov_temp   = msf.ShiftImage(fov_temp, subshift_y[n], subshift_x[n]);
                # Apodize image by FOV
                fov_temp = np.double(fov_temp)/np.max(fov_temp)
                image_temp[:,:,0] = np.double(image_temp[:,:,0])*fov_temp
                image_temp[:,:,1] = np.double(image_temp[:,:,1])*fov_temp
                image_temp[:,:,2] = np.double(image_temp[:,:,2])*fov_temp
                image_data[:,:,:,n] = np.uint8(image_temp)
                fov_frame[:,:,n] = fov_temp
    #Now Create the composite image
    composite_image = np.zeros([max(offset_y)+Ny,max(offset_x)+Nx,3],dtype=np.double())
    composite_gain = np.zeros([max(offset_y)+Ny,max(offset_x)+Nx],dtype=np.double())
    print("Creating Composite Image")
    Ny = np.size(image_temp[:,1,1])
    Nx = np.size(image_temp[1,:,1])
    for n in range(0,N_desired_slots):
        composite_image[(offset_y[n]):(offset_y[n]+Ny),(offset_x[n]):(offset_x[n]+Nx),:] = \
        composite_image[(offset_y[n]):(offset_y[n]+Ny),(offset_x[n]):(offset_x[n]+Nx),:] + \
        np.double(image_data[:,:,:,n])/gain[n];
        composite_gain[(offset_y[n]):(offset_y[n]+Ny),(offset_x[n]):(offset_x[n]+Nx)] = \
        composite_gain[(offset_y[n]):(offset_y[n]+Ny),(offset_x[n]):(offset_x[n]+Nx)] + \
        np.double(fov_frame[:,:,n]);
    composite_gain[composite_gain<.998]=1
    #divide by overlap
    composite_image[:,:,0] = composite_image[:,:,0]/composite_gain
    composite_image[:,:,1] = composite_image[:,:,1]/composite_gain
    composite_image[:,:,2] = composite_image[:,:,2]/composite_gain
    # Apply gamma correction
    composite_image = np.uint8(max_I*(composite_image/max_I)**(1/g))
    plt.figure(0)
    plt.imshow(composite_image)
    plt.title('Before')
    # Run the optiziation function
    print("Determining optimal gain parameters")
    newcomposite, modmat = msf.autoAdjustGain(image_data, fov_frame, offset_x, offset_y, iterations)
    # modmat is an matrix that contains the new apodization profiles for each color channel for each image
    plt.figure(1)
    plt.imshow(newcomposite)
    plt.title('After')


def  check_number_of_features_for_every_camera(pto_filename):
    # return the index for cameras that does not have enough number of features
    # current the camera ids are identical ids in the pto file
    with open(pto_filename) as pto_file:
        pto = pto_file.read()
    pts_list = [0] * 19
    lines = pto.split("\n")
    pts_list = list(filter(lambda x: len(x) > 1 and x[0] == 'c', lines))
    for pts in pts_list:
        tokens = pts.split(" ")
        cam_id = int(tokens[1][1:])
        pts_list[cam_id] += 1
    a = 0
    result_lst = []
    for pts in pts_list:
        if pts < 3:
            result_lst.append(a)
        a += 1
    return result_lst


def copy_reference_features_to_current_pto(prealigned_pto_filename, current_pto_filename, empty_feature_cam_ids):
    # copy the features from first pto file to the second pto file, select the cameras based on emtpy_feature_cam_ids
    camera_feature_dict = {}
    with open(prealigned_pto_fielname) as pto_file:
        prealigned_pto = pto_file.read()
    lines = prealigned_pto.split("\n")
    pts_list = list(filter(lambda x: len(x) > 1 and x[0] == 'c', lines))
    for pts in pts_list:
        tokens = pts.split(" ")
        cam_id = int(tokens[1][1:])
        if cam_id in empty_feature_cam_ids:
            if cam_id not in camera_feature_dict:
                camera_feature_dict[cam_id] = [pts]
            else:
                camera_feature_dict[cam_id].append(pts)
    with open(current_pto_filename) as pto_file:
        current_pto = pro_file.read()
    output_pto_str = ""
    lines = current_pto.split("\n")
    for line in lines:
        if len(line) > 1 and line == 'control points':
           for cam_id in camera_feature_dict.keys():
               for feature_line = camera_feature_dict[cam_id]:
                   output_pto_str = output_pto_str + feature_line + "\n"
        else:
            output_pto_str = output_pto_str + line + "\n"
    with open("pruning_pts_adding_feature.pto", 'w') as output_pto:
        output_pto.write(output_pto_str)

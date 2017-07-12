# kirito

##### This repository contains a set of Python scripts and C/C++ programs for multi-row image stitching.



## Table of Contents
0. [Introduction](#Introduction)
 -  [How do they work?](#how)
1. [Required libraries](#Requirements)
2. [Install OpenCV from source on Ubuntu](#Install-OpenCV)
3. [Run stitching script](#Run)


## Introduction <a name="Introduction"></a>
#### Currently there are three separate stitching process implemented. They are:
1. Completely Hugin-based stitching (recommended)
2. OpenCV + Hugin (not recommended)
3. OpenCV + Hugin + Making use of the global view image (not as robust as process 1. But will be improved later)

#### How do they work? <a name="how"></a>

The program is for speeding up the process of building a camera model. This is done by 1) build a wrapper around Hugin command line tools, along with a GUI interface. 2) apply algorithms implemented in OpenCV.

#### 1. Common points
All three processes take input:

A list of images that can potentially be stitched together.

And produces outputs:
1. optimized.pto: a project file that can be opened by Hugin.
2. model.json: a model file that can be opened by Saccade.

#### 2. Completely Hugin-based stitching
Pure Hugin-based stitching contains the following stages:
1. Initialize project
2. Update the project file to set the crop factor equals 7
3. Generate control points (visual feature locations)
4. Clean up control points by removing ones that are likely to generate false matches
5. Further clean up control points
6. Find vertical lines in the images
7. Run optimization to find a stitching
9. Run Python script to generate a Saccade model file

#### 3. OpenCV + Hugin
In this version of stitching, the feature finding stage is different.
1. Use the program "feature finder" to find the features in all images. Feature finder uses OpenCV library in finding the features. Feature type: ORB/SURF.
2. The features are sent to a Python filter: "filter_features_based_on_locations.py" program. The filter program removes the feature matches if the two features are not in two adjacent images. When two features are in two adjacent images, if they are not on the overlapping region, they are also removed.
3. The features are converted to Hugin format using "parse_output_for_hugin.py."
4. An initialization of Hugin pto file is generated by "generate_hugin_input.py". The program combines the features found in the previous stage with some metadata needed in the pto file.
5. The result pto file is sent to the Hugin feature filter program. This stage is similar to stage 4 in completely Hugin-based stitching.
6. Same as stage 5 in completely Hugin-based stitching.
7. Same as stage 7 in completely Hugin-based stitching.

#### 4. OpenCV + Hugin + global view
This process is similar to OpenCV + Hugin process. Besides that after stage 1 in OpenCV + Hugin process, the features are first sent to another filter "filter_features_based_on_global_view.py". In this program, first only the features in each local view image that matches features in the global view image is kept. Then if there is a direct match between two features in two local view images in this set, and the two features share the same matched feature in the global view, they are considered as a good match. Other matches are ignored. Then the later stages are the same as OpenCV + Hugin process stage 2~7.

## Required libraries <a name="Requirements"></a>
0. You should have Python3 installed in your system.
1. You should have Hugin installed in your system.
2. For process 2 and process 3, you also need to have OpenCV installed and linked to Python3.
3. The program has been tested on Ubuntu 16.04.
4. For running the GUI, PyQt5 is required.

## Install OpenCV from source on Ubuntu <a name="Install-OpenCV"></a>

First upgrade pre-installed packages:
```bash
sudo apt-get update
sudo apt-get upgrade
```

Install developer tools:
```bash
sudo apt-get install build-essential cmake git pkg-config
```

Install image and video libraries and packages:
```bash
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
```

Install GTK:
```bash
sudo apt-get install libatlas-base-dev gfortran
```

Get the Python package manager pip:
```bash
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
```

Install python dev and numpy
```bash
sudo apt-get install python3.4-dev
pip install numpy
```

Install OpenCV 3 with Python bindings
```bash
cd ~
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout 3.0.0

cd ~
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout 3.0.0

cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=OFF \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON \
      -D WITH_CUDA=OFF ..
make -j4
sudo make install
sudo ldconfig

cd ~/usr/local/lib/python3.4/site-packages/
ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so
```

## Run stitching script <a name="Run"></a>
### To run Hugin based stitching with GUI, type
```bash
python3 automatic.py --gui
```
The GUI contains several widgets:
#### Buttons
Stitching: perform the stitching

Open in Hugin: Open Hugin. The Hugin program will try open the optimized.pto file.

Preview: don't run stitching, but show the preview stitched result, assume there is a file "preview.jpg" in the working directory.
#### Checkboxes
Loading existing model file: in Hugin-based stitching, a pre-aligned model can be used in the optimization process. The default pre-aligned model file is "/home/$user/data/mantisModelGen/prealigned.pto". If the default file is not found, a pop-up window will appear to let user select the pre-aligned model file. The default directory can be modified in the \_\_init\_\_() method in main.py

Grab frames: if checked, the program will get frames from the render machine (render machine IP address specified in IP text field). The frames will be saved in the working directory.

Store frame to custom directory: if checked, the program will set the working directory to the one specified in the textfield below the checkbox. Otherwise the default working directory is /home/$user/mantisModelGen/$yeardatetime/.

#### Others:
Slider: user can use slider to select the threshold in finding feature matching. Higher threshold: less picky in finding matches.

max visible scale: the parameter used to determine the max scale for displaying narrow field view camera frames in viewing in V2. Default: 4. The wide field of view camera is always 1000.

radial: the parameter used to determine the order number in displaying narrow field of view camera frames in V2. Default: 10. The wide field of view camera is always 11.

IP: IP address of the render machine.

### To run pure Hugin based stitching, Type
```bash
python3 automatic.py
```

### To run process 2 and 3, first compile the opencv feature finder program in the current directory:
```bash
g++ -ggdb feature_finder.cpp -o feature_finder `pkg-config --cflags --libs opencv`
```

### Then make sure all images are in current directory, in the format xx.xx.xx.xx_sensorX.jpg.
### Type
```bash
python3 automatic_with_opencv.py [threshold for matching: recommend 0.1]
```

### for example:
```bash
python3 automatic_with_opencv.py 0.1
```

### Finally, convert the pto file into Saccade model file:
```bash
python3 HuginMakeSaccadeConfig.py optimized.pto model.json
```

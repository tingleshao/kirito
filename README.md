# kirito

### You should have Hugin installed in your system, and you should current be in a directory with a runnable compiled feature_finder cpp program.

## Install OpenCV from source on Ubuntu

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
git checkout 3.1.0

cd ~
git clone https://github.com/opencv/opencv_contrib.git
git checkout 3.1.0

cd ~/opencv2
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=OFF \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON ..
make -j4
sudo make install
sudo ldconfig

cd ~/usr/local/lib/python3.4/site-packages/
ln -s /usr/local/lib/python3.4/site-packages/cv2.cpython-34m.so cv2.so
```

## Run our script

### To use the tool, first compile the opencv feature finder program in the current directory:
```bash
g++ -ggdb feature_finder.cpp -o feature_finder `pkg-config --cflags --libs opencv`
```

### Then make sure all images are in current directory, in the format xx.xx.xx.xx_sensorX.jpg.
## Type
```bash
python3 automatic_with_opencv.py [threshold for matching: recommend 0.1]
```

### for example:
```bash
python3 automatic_with_opencv.py 0.1
```

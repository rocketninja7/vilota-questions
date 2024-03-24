# My setup
## Linux environment
1. Download VirtualBox from https://www.virtualbox.org/wiki/Downloads. (I already had it downloaded on my machine)
2. Install VirtualBox on the machine.
3. Download Ubuntu Desktop from https://ubuntu.com/download/desktop.
4. Open VirtualBox and click the "New" button. Go to "Expert Mode".
5. Choose the "Type" as "Linux" and the "Version" as "Ubuntu (64-bit)". 
Set the memory size as desired. I set it to 8192MB. 
6. Select "Create a Virtual Hard Disk now" and click "Create".
7. Set the size of virtual hard disk as desired. I set it to 24GB. 
Ensure storage space is "Dynamically allocated". Click "Create".
We return to the original VirtualBox page with a new Virtual Machine.
8. Click on "Settings", then "Storage". Then click on "Empty" below "Controller IDE".
9. Click on the blue disk icon next to the "Optical Drive" selection.
Navigate to where the Ubuntu Desktop .iso file is located.
10. I also went to "General" > "Advanced" to set "Shared Clipboard" to "Bidirectional".
11. Click "Ok" and we return to the original VirtualBox page.
12. Now we press "Start".
13. Select "Try or install Ubuntu".
14. Click "Install Ubuntu".
15. Select the settings you desire. Personally, I used all the defaults other than selecting 
"Minimal installation". When prompted to erase disk and install the OS, just continue.
16. Wait for installation to complete.
17. Click "Restart now" when prompted. Then, press the "Enter" key when prompted. And we are done!

## OICC 
With reference to https://github.com/urbste/OpenImuCameraCalibrator.
1. Open Terminal.
2. Run ```sudo apt-get install libopencv-dev libopencv-contrib-dev```.
3. We also realise we need git, cmake and g++. 
Run ```sudo apt install git``` to install git.
Run ```sudo apt install cmake``` to install cmake.
Run ```sudo apt install g++``` to install g++.
4. In order to build ceres, we also need Eigen. 
We run ```sudo apt install libeigen3-dev``` to install it.
5. To build ceres, we also need glog! 
Referring to https://github.com/google/glog#cmake, 
we can run the following:
```
git clone https://github.com/google/glog.git
cd glog
cmake -S . -B build -G "Unix Makefiles"
cmake --build build
```
We can test our installation with ```cmake --build build --target test```.
Then we install the built files with ```sudo cmake --build build --target install```.
6. Finally, we install ceres with 
```
git clone https://github.com/ceres-solver/ceres-solver
cd ceres-solver
git checkout 2.1.0
mkdir -p build && cd build && cmake .. -DBUILD_EXAMPLES=OFF -DCMAKE_BUILD_TYPE=Release
sudo make -j install
```
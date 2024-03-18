# tflite-facial-expression
 TensorFlow on facial expression for edge devices

This project contains python code for training a machine learning model to identify facial expression.
It is used for Machine Learning module and mobile developement module.

This readme file contains information of the dataset, setup and journey log of this exploration

# Data Set
Training is using AffectNet's dataset and python code can be found in a jupyter notebook in src folder
The data set details is here https://drive.google.com/file/d/141XcApU7gqHoPsbI8G-MyXqZz6eGpO80/view 

Training Data info
Label info: (0: Neutral, 1: Happy, 2: Sad, 3: Surprise, 4: Fear, 5: Disgust, 6: Anger, 7: Contempt)
<br>Neutral: 74874 (26.02%)
<br>Happy: 134416 (46.72%)
<br>Sad: 25461 (8.85%)
<br>Surprise: 14093 (4.90%)
<br>Fear: 6382 (2.22%)
<br>Disgust: 2808 (1.32%)
<br>Anger: 24888 (8.65%)
<br>Contempt: 3757 (1.31%)

# Setup
This project will require the host to have a GPU device working on windows 10 or later version.
The base of the project is using python3 in anaconda. Follow the instructions below to install the project:
1. Install Anaconda/Miniconda
2. Create a conda environment
3. Clone this git repo into the conda environment folder, this repo will only contain code and text notes
4. Make a folder named "asset" in the conda environment folder, install and unzip train_set.tar and val_set.tar into the folder. These 2 files can be found in https://onedrive.live.com/?authkey=%21ABotnQhy7%2Dg2sRE&id=71A021B981CFE85B%21136507&cid=71A021B981CFE85B
5. Open command prompt and activate the conda environment created. The next few steps will be performed in the command prompt
6. Install python first with "conda install -y python=3.10"
6. Install tensorflow gpu with "pip install tensorflow-gpu==2.8"
7. Just to ensure some modules are installed properly, use "pip install protobuf==4.23 h5py==3.10"
8. Install the remaining packages with conda, "conda install -y jupyter numpy opencv matplotlib cudnn=8.1 cudatoolkit=11.2"
9. All code will be performed using jupyter lab, thus when you are in the conda environment in code, type "jupyter lab" to activate the notebook. Navigate to the repo directory and create your own jupyter notebook, start coding away!

# Problems, Journey and Solutions
Throughout the exploration of neural network on facial expression, there were several experiments attempted and issues faced, resulting in solution found or path discontinued. Here is the log of the issues found to prevent repeat of facing same issue

## Problem 1
GPU kept running out of RAM, unable to train model effectively as OOM error kept appearing
### Journey 
Explored multiprocessing in python, GPU "per_process_gpu_memory_fraction" configuration and cuda reset. <br>
Multiprocessing and GPU does not work, memory still remain high. Cuda reset will erase the data in gpu, but crashing the system too.

### Solution
Resetting Keras session worked, with:
'''
    sess = get_session()
    clear_session()
    sess.close()
    sess = get_session()
'''

## Problem 2
Difficulty in further preprocessing data converted by media pipe due to ambiguity in image. 

### Journey
Preprocessing data after using media pipe's facial landmark extraction, such as finding distance between irises and eye or distance between left and right eyebrow. Media pipe allowed us to extract the important facial landmarks, however, some images provided by affectnet are ambiguous, where images that looks like happy is labeled neural. <br>

### Solution
1. First solution is to manually select the data, doing further data clean up on our own. 

2. Second solution is to select the data using more advance selection algorithm, for example, discarding happy face images with mouth vertices that matches that of frowning mouth.

3. Third solution can be using CNN to do feature extractions. The hope is that CNN might uncover some similarity in the facial images.








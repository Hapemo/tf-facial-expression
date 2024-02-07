# tflite-facial-expression
 TensorFlow on facial expression for edge devices

This project contains python code for training a machine learning model to identify facial expression.
It is used for Machine Learning module and mobile developement module.


# Data Set
Training is using AffectNet's dataset and python code can be found in a jupyter notebook in src folder
The data set details is here https://drive.google.com/file/d/141XcApU7gqHoPsbI8G-MyXqZz6eGpO80/view 

Training Data info
Label info: (0: Neutral, 1: Happy, 2: Sad, 3: Surprise, 4: Fear, 5: Disgust, 6: Anger, 7: Contempt)
Data Count
Neutral: 74874 (26.02%)
Happy: 134416 (46.72%)
Sad: 25461 (8.85%)
Surprise: 14093 (4.90%)
Fear: 6382 (2.22%)
Disgust: 2808 (1.32%)
Anger: 24888 (8.65%)
Contempt: 3757 (1.31%)

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














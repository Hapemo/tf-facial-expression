import os
import numpy as np

def Setup():
    os.chdir("C:\\Users\\jazzt\\anaconda3\\envs\\tflite-facial-expression\\asset") # change working directory

# Load the images into a nested list containing info of image in tuple format (image name, valence, arousal)
def LoadImageNames(imageFiles):
    trainingSet = [[]for i in range(8)]
    loadCounter = 0
    for file in imageFiles:
        loadCounter += 1
        if (loadCounter%10000==0):
            print("Files loaded:{}".format(loadCounter))
            if (loadCounter > 30000):
                break
        name = file.name[:-4] # file name w/o file extension
        data = np.load("train_set\\annotations\\{}_exp.npy".format(name))
        trainingSet[int(data.item(0))].append(file.name)
    return trainingSet

# # Path directories
# Setup()
# # annotationPath = os.getcwd() + "\\train_set\\annotations\\"
# # imagePath = os.getcwd() + "\\train_set\\images"

# # Numpy load
# # data = np.load(annotationPath + "191_lnd.npy")

# #Loop through all the files and get file number
# imageFiles = os.scandir("train_set\\images")
# trainingSet = LoadImageNames(imageFiles)

# print(trainingSet)
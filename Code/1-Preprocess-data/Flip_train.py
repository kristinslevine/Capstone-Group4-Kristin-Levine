import numpy as np
import pandas as pd
import os
from glob import glob
import shutil
import cv2

#DataFolders
data_folder = "/Users/kristinlevine/Desktop/flip_train"

data_mild = data_folder + "/MildDemented/"
data_mod = data_folder + "/ModerateDemented/"
data_non = data_folder + "/NonDemented/"
data_very = data_folder + "/VeryMildDemented/"

print('Number of MildDemented:', len(os.listdir(data_mild)))
print('Number of ModerateDemented:', len(os.listdir(data_mod)))
print('Number of NonDemented:', len(os.listdir(data_non)))
print('Number of VeryMildDemented:', len(os.listdir(data_very)))
print('\n')

# Flipping images
#balancing dataset as much as possible with the flipping
# data_mod will still be the smallest

#Mild Class
#Flipping images: 0
for path in [f for f in os.listdir(data_mild) if f[-4:] == ".jpg"]:
    img = cv2.flip(cv2.imread(data_mild + path), 0)
    filename = path + '_flip.jpg'
    cv2.imwrite(os.path.join(data_mild, filename), img)

#Flipping images: 1
for path in [f for f in os.listdir(data_mild) if f[-4:] == ".jpg"]:
    img = cv2.flip(cv2.imread(data_mild + path), 1)
    filename = path + '_flip.jpg'
    cv2.imwrite(os.path.join(data_mild, filename), img)

#Flipping images: -1
for path in [f for f in os.listdir(data_mild) if f[-4:] == ".jpg"]:
    img = cv2.flip(cv2.imread(data_mild + path), -1)
    filename = path + '_flip.jpg'
    cv2.imwrite(os.path.join(data_mild, filename), img)

#Mod Class
#Flipping images: 0
for path in [f for f in os.listdir(data_mod) if f[-4:] == ".jpg"]:
    img = cv2.flip(cv2.imread(data_mod + path), 0)
    filename = path + '_flip.jpg'
    cv2.imwrite(os.path.join(data_mod, filename), img)

#Flipping images: 1
for path in [f for f in os.listdir(data_mod) if f[-4:] == ".jpg"]:
    img = cv2.flip(cv2.imread(data_mod + path), 1)
    filename = path + '_flip.jpg'
    cv2.imwrite(os.path.join(data_mod, filename), img)

#Flipping images: -1
for path in [f for f in os.listdir(data_mod) if f[-4:] == ".jpg"]:
    img = cv2.flip(cv2.imread(data_mod + path), -1)
    filename = path + '_flip.jpg'
    cv2.imwrite(os.path.join(data_mod, filename), img)

#Non Class
#Flipping images: 1
for path in [f for f in os.listdir(data_non)[0:216] if f[-4:] == ".jpg"]:
    img = cv2.flip(cv2.imread(data_non + path), 1)
    filename = path + '_flip.jpg'
    cv2.imwrite(os.path.join(data_non, filename), img)

#Very Class
#Flipping images: 1
for path in [f for f in os.listdir(data_very)[0:754] if f[-4:] == ".jpg"]:
    img = cv2.flip(cv2.imread(data_very + path), 1)
    filename = path + '_flip.jpg'
    cv2.imwrite(os.path.join(data_very, filename), img)


print('Number of MildDemented:', len(os.listdir(data_mild)))
print('Number of ModerateDemented:', len(os.listdir(data_mod)))
print('Number of NonDemented:', len(os.listdir(data_non)))
print('Number of VeryMildDemented:', len(os.listdir(data_very)))
print('\n')

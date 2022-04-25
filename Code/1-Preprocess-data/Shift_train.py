import numpy as np
import pandas as pd
import os
from glob import glob
import shutil
import cv2

#DataFolders
data_folder = "/Users/kristinlevine/Desktop/train"

data_mild = data_folder + "/MildDemented/"
data_mod = data_folder + "/ModerateDemented/"
data_non = data_folder + "/NonDemented/"
data_very = data_folder + "/VeryMildDemented/"

save_folder = "/Users/kristinlevine/Desktop/shift_train"
save_mild = save_folder + "/MildDemented/"
save_mod = save_folder + "/ModerateDemented/"
save_non = save_folder + "/NonDemented/"
save_very = save_folder + "/VeryMildDemented/"

print('Number of MildDemented:', len(os.listdir(data_mild)))
print('Number of ModerateDemented:', len(os.listdir(data_mod)))
print('Number of NonDemented:', len(os.listdir(data_non)))
print('Number of VeryMildDemented:', len(os.listdir(data_very)))
print('\n')

#Mild Class

M = np.float32([[1, 0, 5], [0, 1, 10]])
for path in [f for f in os.listdir(data_mild) if f[-4:] == ".jpg"]:
    img = cv2.warpAffine(cv2.imread(data_mild + path), M, (224, 224))
    filename = path + 'shift1.jpg'
    cv2.imwrite(os.path.join(save_mild, filename), img)

M = np.float32([[1, 0, 10], [0, 1, 5]])
for path in [f for f in os.listdir(data_mild) if f[-4:] == ".jpg"]:
    img = cv2.warpAffine(cv2.imread(data_mild + path), M, (224, 224))
    filename = path + 'shift2.jpg'
    cv2.imwrite(os.path.join(save_mild, filename), img)

M = np.float32([[1, 0, 15], [0, 1, 20]])
for path in [f for f in os.listdir(data_mild) if f[-4:] == ".jpg"]:
    img = cv2.warpAffine(cv2.imread(data_mild + path), M, (224, 224))
    filename = path + 'shift3.jpg'
    cv2.imwrite(os.path.join(save_mild, filename), img)

#Mod Class
a = np.arange(5, 280, 5)
b = a*2

for i in range(len(a)):
  M = np.float32([[1, 0, a[i]], [0, 1, b[i]]])
  for path in [f for f in os.listdir(data_mod) if f[-4:] == ".jpg"]:
    img = cv2.warpAffine(cv2.imread(data_mod + path), M, (224, 224))
    filename = path + '_shift' + str(i) + '.jpg'
    cv2.imwrite(os.path.join(save_mod, filename), img)

#Non Class
#shifting image by (5, 10)
M = np.float32([[1, 0, 5], [0, 1, 10]])
for path in [f for f in os.listdir(data_non)[0:216] if f[-4:] == ".jpg"]:
    img = cv2.warpAffine(cv2.imread(data_non + path), M, (224, 224))
    filename = path + '_shift1.jpg'
    cv2.imwrite(os.path.join(save_non, filename), img)

#Very Class
for path in [f for f in os.listdir(data_very)[0:754] if f[-4:] == ".jpg"]:
    img = cv2.warpAffine(cv2.imread(data_very + path), M, (224, 224))
    filename = path + '_shift1.jpg'
    cv2.imwrite(os.path.join(save_very, filename), img)

print('Number of MildDemented:', len(os.listdir(save_mild)))
print('Number of ModerateDemented:', len(os.listdir(save_mod)))
print('Number of NonDemented:', len(os.listdir(save_non)))
print('Number of VeryMildDemented:', len(os.listdir(save_very)))
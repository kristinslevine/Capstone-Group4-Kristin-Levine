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

print('Number of MildDemented:', len(os.listdir(data_mild)))
print('Number of ModerateDemented:', len(os.listdir(data_mod)))
print('Number of NonDemented:', len(os.listdir(data_non)))
print('Number of VeryMildDemented:', len(os.listdir(data_very)))
print('\n')

#To create a validation set that I will NOT augment
all_mild_paths = [
    os.path.join(os.getcwd(), data_mild, x)
    for x in os.listdir(data_mild)]

all_mod_paths = [
    os.path.join(os.getcwd(), data_mod, x)
    for x in os.listdir(data_mod)]

all_non_paths = [
    os.path.join(os.getcwd(), data_non, x)
    for x in os.listdir(data_non)]

all_very_paths = [
    os.path.join(os.getcwd(), data_very, x)
    for x in os.listdir(data_very)]

print(len(all_mild_paths))
print(len(all_mod_paths))
print(len(all_non_paths))
print(len(all_very_paths))

#Split to make a val set that is 0.3 of train set

a = round(len(all_mild_paths)*0.3)
b = round(len(all_mod_paths)*0.3)
c = round(len(all_non_paths)*0.3)
d = round(len(all_very_paths)*0.3)

save_folder = "/Users/kristinlevine/Desktop/val"
directory = os.path.dirname(save_folder)
if not os.path.exists(directory):
    os.makedirs(directory)

save_mild = save_folder + "/MildDemented/"
save_mod = save_folder + "/ModerateDemented/"
save_non = save_folder + "/NonDemented/"
save_very = save_folder + "/VeryMildDemented/"

save_directories = [save_mild, save_mod, save_non, save_very]
for i in range(len(save_directories)):
    directory = os.path.dirname(save_directories[i])
    if not os.path.exists(directory):
        os.makedirs(directory)

for files in all_mild_paths[0:a]:
    shutil.move(files, save_folder + "/MildDemented/")

for files in all_mod_paths[0:b]:
    shutil.move(files, save_folder + "/ModerateDemented/")

for files in all_non_paths[0:c]:
    shutil.move(files, save_folder + "/NonDemented/")

for files in all_very_paths[0:d]:
    shutil.move(files, save_folder + "/VeryMildDemented/")

print("Train Set")
print('Number of MildDemented:', len(os.listdir(data_mild)))
print('Number of ModerateDemented:', len(os.listdir(data_mod)))
print('Number of NonDemented:', len(os.listdir(data_non)))
print('Number of VeryMildDemented:', len(os.listdir(data_very)))
print('\n')

print("Val Set")
print('Number of MildDemented:', len(os.listdir(save_folder + "/MildDemented/")))
print('Number of ModerateDemented:', len(os.listdir(save_folder + "/ModerateDemented/")))
print('Number of NonDemented:', len(os.listdir(save_folder + "/NonDemented/")))
print('Number of VeryMildDemented:', len(os.listdir(save_folder + "/VeryMildDemented/")))
print('\n')


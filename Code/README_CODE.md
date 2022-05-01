README for CODE FOLDERS

Data for this project can be downloaded at:
https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images


**1-Preprocess-data** -- use the files in this folder to create a separate validatation dataset, as well as create the flipped and shifted test sets

Make_val_set.py: 
1. After downloading the data, set the path to the train folder.
2. Run this file to create a separate validation set.

Flip_train.py: 
1. Make sure you have run "Make_val_set.py" first to create the validation set.
2. Make a copy of the train folder and rename it "flip_train"
3. Set the path to the original "train" and the "flip_train" folder
4. Run this file to augment the data by flipping the images

Shift_train.py: 
1. Make sure you have run "Make_val_set.py" first to create the validation set.
2. Make a copy of the train folder and rename it "shift_train"
3. Set the path to the original "train" and the "shift_train" folder
4. Run this file to augment the data by shifting the images

**2-Create-Models-No-Augmentation**

This folder contains three files using non-augmented data: ResNet50, VGG16, Xception

For each file: 

1. Change the paths to the abspath_curr, original train, val, and test folders 
3. Run the file to train the model

**3-Create-Models-Flipped**

This folder contains three files using flipped-augmented data: ResNet50, VGG16, Xception

For each file: 

1. Change the paths to the abspath_curr, flip_train, val, and test folders 
3. Run the file to train the model

**4-Create-Models-Shifted**


This folder contains three files using shifted-augmented data: ResNet50, VGG16, Xception

For each file: 

1. Change the paths to the abspath_curr, shift_train, val, and test folders 
3. Run the file to train the model

**5-Ensemble-Best-Models**

For each file:

1. Change the path to your abspath_curr and test folder 
2. Run the file to ensemble the models

**6-Other-Dataset_Explorations**

Note: I used ADNI images for these files; researchers can apply for access at https://adni.loni.usc.edu/

These are not ALL the files I used in my explorations -- just a sampling.

Preprocess_63_Slices -- example of how I extracted slices from MRI images
MRI_Xception -- example of one of the models with excellent train/val accuracy, but very poor test accuracy
MRI_Combine_Models -- example of how I attempted to created patient-wise (not slice-wise) accuracy
AD_Kaggle_Model_FreeSurfer_Preprocess -- example of how I explored the ADNI FreeSurfer images, trying to explore which ones had the more information for the model

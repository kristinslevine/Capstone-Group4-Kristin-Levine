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

change the paths to the original train, val, and test datasets (cells___)
also make note of the path you choose to save your model
if you wish, adjust paths for saving the graphs

**3-Create-Models-Flipped**

change the paths to the original train, val, and flip_train datasets (cells___)
also make note of the path you choose to save your model
if you wish, adjust paths for saving the graphs

**4-Create-Models-Shifted**

change the paths to the original train, val, and shift datasets (cells___)
also make note of the path you choose to save your model
if you wish, adjust paths for saving the graphs

**5-Ensemble-Best-Models**

change the path to your test datset (cell__)
changes the paths to your created models (cell__)

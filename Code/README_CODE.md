README for CODE FOLDERS

Data for this project can be downloaded at:
https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images


**1-Preprocess-data** -- use the files in this folder to create a separate validatation dataset, as well as create the flipped and shifted test sets

Make_val_set.py: 
1. After downloading the data, set the path to the train folder.
2. Run this file to create a separate validation set.

Flip_train.py: After you have run "Make_val_set.py" copy the test dataset and remain it flip_train. Then run this file

Shift_train.py: Copy the original test dataset again and rename it shift-train. Then run this file

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

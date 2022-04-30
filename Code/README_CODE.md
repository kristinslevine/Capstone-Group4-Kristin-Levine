README for CODE FOLDERS

Data for this project can be downloaded at:
https://www.kaggle.com/tourist55/alzheimers-dataset-4-class-of-images

1-Preprocess-data -- use the files in this folder to create a separate validatation dataset, as well as create the flipped and shifted test sets

**Make_val_set.py**
After downloading the data, run this file to create a separate validation set.

**Flip_train.py**
After you have run "Make_val_set.py" copy the test dataset and remain it flip_train/n
Then run this file

**Shift_train.py**
Copy the original test dataset again and rename it shift-train
Then run this file

2-Create-Models-No-Augmentation

3-Create-Models-Flipped

4-Create-Models-Shifted

5-Ensemble-Best-Models

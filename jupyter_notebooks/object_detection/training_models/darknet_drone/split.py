import pathlib
import random
import shutil
import os

IMG_PATH = r'../images'
LABELS_PATH = r'../annotations_txt'
train_val = r'../trainval.txt'
DARKNET_IMG_PATH = r'images'

with open(train_val, 'r') as f:
    train_val_paths = f.read().split('\n')

# for item in os.listdir(IMG_PATH):
#     file_name = os.path.join(IMG_PATH, item)
#     dest = os.path.join(DARKNET_IMG_PATH, item)
#     if os.path.isfile(file_name):
#         shutil.copy(file_name, dest)
        
# for item in os.listdir(LABELS_PATH):
#     file_name = os.path.join(LABELS_PATH, item)
#     dest = os.path.join(DARKNET_IMG_PATH, item)
#     if os.path.isfile(file_name):
#         shutil.copy(file_name, dest)


# our own split.
random.seed(42)
random.shuffle(train_val_paths)
num_examples = len(train_val_paths)
num_train = int(0.9 * num_examples)
train_examples = train_val_paths[:num_train]
val_examples = train_val_paths[num_train:]

with open('train.txt', 'w') as f_train:
    _ = [f_train.write(os.path.abspath(IMG_PATH) + "/" + train_example + '.jpg' + "\n") for train_example in train_examples]
    
with open('test.txt', 'w') as f_test:
    _ = [f_test.write(os.path.abspath(IMG_PATH) + "/" + test_example + ".jpg" + "\n") for test_example in val_examples]



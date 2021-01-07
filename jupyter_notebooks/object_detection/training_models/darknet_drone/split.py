import pathlib
import random
import shutil
import os

OLD_IMG_PATH = r'../images_bak'
IMG_PATH = r'../images'
LABELS_PATH = r'../labels'
OLD_LABELS_PATH = r'../labels_bak'
orig_train_val = r'../orig_trainval.txt'
train_val = r'../trainval.txt'



# with open(orig_train_val, 'r') as f:
#     train_val_paths = f.read().split('\n').pop()

# with open(train_val, 'w') as f:
#     for idx, train_val_path in enumerate(train_val_paths):
#         shutil.copy(os.path.join(OLD_IMG_PATH, train_val_path + ".jpg"), os.path.join(IMG_PATH, f"{idx}.jpg"))
#         shutil.copy(os.path.join(OLD_LABELS_PATH, train_val_path + ".txt"), os.path.join(LABELS_PATH, f"{idx}.txt"))
#         f.write(f"{idx}\n")
    
    

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

with open(train_val, 'r') as f:
    train_val_paths = f.read().split('\n')[:-1]
# print(train_val_paths)

# our own split.
random.seed(42)
random.shuffle(train_val_paths)
num_examples = len(train_val_paths)
num_train = int(0.9 * num_examples)
train_examples = train_val_paths[:num_train]
val_examples = train_val_paths[num_train:]

with open('train.txt', 'w') as f_train:
    _ = [f_train.write(os.path.join(os.path.abspath(IMG_PATH), train_example + '.jpg') + "\n") for train_example in train_examples]
    # _ = [f_train.write(f"{os.path.join(os.path.abspath(IMG_PATH), train_example + '.jpg')}" + '\n') for train_example in train_examples]
    
with open('test.txt', 'w') as f_test:
    _ = [f_test.write(os.path.abspath(IMG_PATH) + "/" + test_example + ".jpg" + "\n") for test_example in val_examples]



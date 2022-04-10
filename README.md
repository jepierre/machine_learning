# machine_learning


# Getting Started

install anaconda

update anaconda 
conda update -n base -c defaults conda

create environement from tensorflow
conda create -n ml_tf tensorflow

test tensorflow
python -c "import tensorflow as tf; print(tf.__git_version__, tf.__version__)"
unknown 2.6.0

test keras
python -c "import keras; print(keras.__version__)"


First install tensorflow and pytorch
conda install -n ml_tf -c pytorch pytorch

test pytorch
python -c "import torch; print(torch.__version__)"

#TODO: 
create ann to model simple addition
y = x1 + x2
model architecture will be 2-2-1, expected MSE=1.6e-8, R=1

create ann to model sin function
y = sin(x)
model architecture will be 1-2-1, expected MSE = 1.4e-5, R=1

create ann to model bessel function, y = J_3(x)
model architecture will 1-2-1, R=.29, MSE=0.014
modle architecture will 1-18-1, R=.98, MSE=0.00064

use 100 data points, 75 training, 25 test

calculate R using pearson correlation coefficient

# references
[Machine Learning with Tensorflow](https://github.com/BinRoot/TensorFlow-Book/blob/master/ch09_cnn/Concept03_cnn.ipynb)

[tensorflow with ros](https://github.com/osrf/tensorflow_object_detector)

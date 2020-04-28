To set windws path
`set PYTHONPATH=%PYTHONPATH%;%cd%;%cd%\research\slim`

create tf_record  
```python research\object_detection\dataset_tools\create_drone_tf_record.py```

run training
```
python research\object_detection\model_main.py --alsologtostderr --model_dir=train\ --pipeline_config_path=ssd_mobilenet_v2_coco.config
```

start tensorfboard
tensorboard --logdir=./ in models directory

run with numpy==1.16
pip intall numpy==1.16

use this tutorial
[Training Custom Object Detector](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html#creating-tensorflow-records)


## Links
[drone detectaion database](https://github.com/Futi7/Drone-Detection?files=1)
[labelImg](https://github.com/tzutalin/labelImg)
[custom object detector](https://becominghuman.ai/tensorflow-object-detection-api-tutorial-training-and-evaluating-custom-object-detector-ed2594afcf73)  

[yolo to tf records](https://github.com/mwindowshz/YoloToTfRecords)
[using tensorfboard with keras](https://www.tensorflow.org/tensorboard/get_started)
[using own dataset](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md)  
[train a racoon detector](https://towardsdatascience.com/how-to-train-your-own-object-detector-with-tensorflows-object-detector-api-bec72ecfe1d9)
[racoon dataset](https://github.com/datitran/raccoon_dataset)
[another one, train card detector](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10)
[tf run locally](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_locally.md)

# to get started
* install tensorflow and prerequisites
[install tensorflow detection](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#general-remarks)
make sure to install tensorflow-gpu=1.4


# install tensorflow-gpu=1.4
pip install tensorflow-gpu==1.4
# install dependencies
pip install numpy==1.16
pip install pillow, lxml, jupyter, matplotlib, opencv, cython


get dataset
wget https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/zcsj2g2m4c-4.zip

unzip files
unzip zcsj2g2m4c-4.zip -d drone_set
cd drone_set
unzip Database1.zip

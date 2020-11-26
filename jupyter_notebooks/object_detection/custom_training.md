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
and [this](https://towardsdatascience.com/custom-object-detection-using-tensorflow-from-scratch-e61da2e10087)


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
[drone detection with maskrcnn](https://towardsdatascience.com/object-drones-detection-step-by-step-guide-on-mask-r-cnn-7bec0fb09a1)

# to get started
* install tensorflow and prerequisites
[install tensorflow detection](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#general-remarks)
make sure to install tensorflow-gpu=1.4

# log into machine
ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -L 8889:localhost:8887 -L 6008:localhost:6007 jpierre@moons.cs.unm.edu -t ssh -L 8887:localhost:1234 -L 6007:localhost:1235 jpierre@lore.cs.unm.edu


# install tensorflow-gpu=1.4
pip install tensorflow-gpu==1.4
# install dependencies
pip install numpy==1.16
pip install pillow, lxml, jupyter, matplotlib, opencv, cython, contextlib2


get dataset
wget https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/zcsj2g2m4c-4.zip

or use [drone-net dataset](https://github.com/chuanenlin/drone-net)

unzip files
unzip zcsj2g2m4c-4.zip -d drone_set
cd drone_set
unzip Database1.zip

use script to convert yolo to voc files
[yolo_to_voc](https://gist.github.com/goodhamgupta/7ca514458d24af980669b8b1c8bcdafd)

get ssd checkpoint
wget download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz
tar -xvf ssd_mobilenet_v2_coco_2018_03_29.tar.gz

copy model checkpoints
cp model.ckpt.index model.ckpt.meta model.ckpt.data-00000-of-00001 ../checkpoints/


install pycocotools
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
cp -r pycocotools <PATH_TO_TF>/TensorFlow/models/research/

# convert yolo to voc

# create tf records
python create_drone_tf_record.py


create temp folder
mkdir temp
export TMPDIR=temp
tensorboard --logdir=training --port=1235

to run
python model_main.py --alsologtostderr --model_dir=training/ --pipeline_config_path=ssd_mobilenet_v2_coco.config


# export graph
python .\export_inference_graph.py --input_type image_tensor --pipeline_config_path .\ssd_mobilenet_v2_coco.config --trained_checkpoint_prefix .\training\model.ckpt-3680 --output_directory trained-inference-graphs/gpu_output_inference_graph_v1.pb

python export_inference_graph.py --input_type image_tensor --pipeline_config_path ssd_mobilenet_v2_coco.config --trained_checkpoint_prefix training/model.ckpt-<> --output_directory trained-inference-graphs/gpu_output_inference_graph_v2.pb


[download youtube videos](http://www.youtube-video-downloader.xyz/download?video=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DXdlmoLAbbiQ)

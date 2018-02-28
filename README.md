# The RobotriX

## Paper

The dataset's paper is available as a preprint in arXiv here [The RobotriX: An eXtremely Photorealistic and Very Large-Scale Indoor Dataset of Sequences with Robot Trajectories and Interactions](#).

If you are inspired by or use The RobotriX data or code, please cite:

```
@article{Garcia-Garcia2018,
  title={{The RobotriX}: An eXtremely Photorealistic and Very Large-Scale Indoor Dataset of Sequences with Robot Trajectories and Interactions},
  author={Garcia-Garcia, Alberto and Martinez-Gonzalez, Pablo and Oprea, Sergiu and Castro-Vargas, John and Orts-Escolano, Sergio and Garcia-Rodriguez, Jose},
  journal={arXiv preprint},
  year={2018}
}
```

## Data

| Type      | #0    | #1    | #2    | #3      | #4      | #5    | #6    | #7    | #8    | #9    |
| --------- | ----- | ----- | ----- | ------  | ------- | ----- | ----- | ----- | ----- | ----- |
| Semantic  | void  | wall  | floor | ceiling | window  | door  | table | chair | lamp  | sofa  |
| Detection | -     | -     | -     | -       | -       | -     | table | chair | lamp  | sofa  |

### Raw Data

### Ground Truth

### Download Links

To be released.

## Tools

In this repository, we release all the tools that were used to record and generate our data and ground truth. The reason is twofold: (1) by using the tools anyone can easily reproduce our dataset and (2) anyone can modify or extend our data or generate new datasets for specific problems.

The codebase is divided into different parts:
* data
* server
* client
* generator
* assets
* utils

### Server

### Client

The client side contains the code to reproduce recorded sequences and issue the needed commands using UnrealCV's client to an Unreal Engine server with UnrealCV's plugin to position the camera, the objects, and the robot on each frame and generate raw visual data: RGB, depth map, and instance segmentation mask.

#### Requirements

The following requirements must be met to execute the client:

* Python >= 2.7
  * json
  * numpy
  * matplotlib
  * pillow
* UnrealCV 0.3.10

#### Before Executing

The client takes three JSON files input for configuration: ```client/config.json```, ```client/classes.json```, and ```client/instance_class.json```. Each one of them must be carefully reviewed before executing it.

The first ```config.json``` file specifies various generic configuration options regarding ```unrealengine``` (host IP and port for the Unreal Engine server), the ```scene``` (path to the sequence recording file, usually to be placed inside ```data/```), and the ```camera``` (calibration parameters ```fx```, ```cx```, ```fy```, ```cy```, ```fov```, and min/max distances in meters for depth generation ```depthmin``` and ```depthmax``` respectively). Make sure to provide the appropriate values for each one of them.

The other two configuration files ```classes.json``` and ```instance_class.json``` are less likely to be modified. The first one provides information for each class of the dataset such as its ```name```, the corresponding semantic (```semantic_class```) and detection (```detection_class```) classes, and the associated ```color``` in RGB format. The second one is just a map that associates each instance name for the objects and meshes in UnrealEngine to a corresponding class. These two files can be modified for various purposes: rearranging classes, adding new ones or removing existing ones, changing their colors...


#### Execution

To execute the client, just execute `python client.py` inside the `client/` directory. It requires the Unreal Engine server to be up and running with the scene in ```Play``` mode (we have detected a performance increase if you do not eject from the window when playing). The client will start replaying the sequence file frame by frame and making the appropriate UnrealCV calls to generate data.

#### After Executing

After the client has finished, three folders (```/rgb```, ```/depth```, and ```/mask```) and three JSON files (```camera.json```, ```sequence.json```, and ```objects.json```) will be created in the ```data/sequence_name``` folder where ```sequence_name``` is the name of the sequence specified in the sequence recording JSON file that was used as input for the client.

The ```/rgb``` folder contains the color maps in 24-bit RGB PNG format. The ```/depth``` directory contains the depth maps in 16-bit grayscale PNGs. The ```/mask``` one contains the instance segmentation masks in 24-bit RGB PNG format. The ```sequence.json``` file is a copy of the original sequence recording file for future reference. ```objects.json``` contains information for each object in the sequence (the given instance name by Unreal Engine ```instance_name```, the class information correlated with the ```classes.json``` and ```instance_class.json``` files, and its instance color given by UnrealCV ```instance_color``` in RGB. The ```camera.json``` contains all the camera information from the previous ```config.json```. 

### Generator

### Assets

### Utils

## Known Issues and Troubleshooting

## License

Both the data and the code for The RobotriX are released under the [MIT license](LICENSE).

## Contact

Please contact Albert Garcia at [albertgg93@gmail.com](mailto:albertgg93@gmail.com) if you have any questions or requests.

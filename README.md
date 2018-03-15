# The RobotriX

[c0]: https://placehold.it/15/f03c15/000000?text=+

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

| Type | 00 <br> ![c0] | 01 <br> ![c0] | 02 <br> ![c0] | 03 <br> ![c0] | 04 <br> ![c0] | 05 <br> ![c0] | 06 <br> ![c0] | 07 <br> ![c0] | 08 <br> ![c0] | 09 <br> ![c0] | 10 <br> ![c0]  | 11 <br> ![c0]  | 12 <br> ![c0]  |
| - | - | - | - | - | - | - | - | - | - | - | -  | -  | -  |
| Semantic  | void  | wall  | floor | ceiling | window  | door  | table | chair | lamp  | sofa  | cupboard | screen | hand |
| Detection | -     | -     | -     | -       | -       | -     | table | chair | lamp  | sofa  | cupboard | screen | hand |

| Type | 13 <br> ![c0] | 14 <br> ![c0] | 15 <br> ![c0] | 16 <br> ![c0] | 17 <br> ![c0] | 18 <br> ![c0] | 19 <br> ![c0] | 20 <br> ![c0] | 21 <br> ![c0] | 22 <br> ![c0] | 23 <br> ![c0] | 24 <br> ![c0] | 25 <br> ![c0]  |
| - | - | - | - | - | - | - | - | - | - | - | -  | -  | -  |
| Semantic  | frame  | bed   | fridge | whiteboard | book | bottle | plant | furniture | toilet | phone | bathtub | cup | mat |
| Detection | frame  | bed   | fridge | whiteboard | book | bottle | plant | - | lamp  | toilet | phone | bathtub | cup | mat |

| Type | 26 <br> ![c0] | 27 <br> ![c0] | 28 <br> ![c0] | 29 <br> ![c0] | 30 <br> ![c0] | 31 <br> ![c0] | 32 <br> ![c0] | 33 <br> ![c0] | 34 <br> ![c0] | 35 <br> ![c0] | 36 <br> ![c0] | 37 <br> ![c0] | 38 <br> ![c0]  |
| - | - | - | - | - | - | - | - | - | - | - | -  | -  | -  |
| Semantic  | mirror | sink  | box | mouse | keyboard | bin | cushion | shelf | bag | curtain | kitchen_stuff | bath_stuff | prop |
| Detection | mirror | sink  | box | mouse | keyboard | bin | cushion | shelf | bag | - | kitchen_stuff | bath_stuff | prop |


### Raw Data

### Ground Truth

### Download Links

To be released.

## Tools

In this repository, we release all the tools that were used to record and generate our data and ground truth. The reason is twofold: (1) by using the tools anyone can easily reproduce our dataset and (2) anyone can modify or extend our data or generate new datasets for specific problems.

The codebase is divided into different parts:
* data
* server
* scene parser
* instance mapper
* client
* generator
* assets
* utils

### Server

The server side contains the code to track all objects, cameras, and bones in an Unreal Engine scene and dump their identifiers, positions, rotations, and bounding boxes. This code implements an Actor in Unreal Engine tack ticks for each rendered frame and gathers all that information by iterating over cameras, actors, and bones.

#### Requirements

* Unreal Engine 4.18
* Visual Studio 2017 with developer tools (for compiling the project).

#### Before Executing

To make the tracker work, we first need to create a new C/C++ class (Actor) in the project content browser. Make sure to name it Tracker and then open the Visual Studio project to copy the content of `./server/Tracker.h` and `./server/Tracker.cpp` into the corresponding project files.

The `.cpp` can be copied directly but for the header file one must take into account that the class name depends on the project name so special attention is required to copy it. For instance, the following code fragment shows the initial part of the `Tracker.h` file for an UE4 project named HamburgHaus (notice the `class HAMBURGHAUS_API` line):

```
#include "Tracker.generated.h"

UCLASS()
class HAMBURGHAUS_API ATracker : public AActor
{
        GENERATED_BODY()
```

That `HAMBURGHAUS_API` prefix must be changed accordingly to the project name, e.g., for a project named InteractiveHouse it would be `INTERACTIVEHOUSE_API`.

After copying the source files, we can modify two important variables in `Tracker.h`, namely `m_save_directory` and `m_file_name`. Those two will control the path to which the tracker will dump the file with the specified name respectively.

Once all the changes are done, just build the scene project either using Visual Studio 2017 or Unreal Engine's button. Once the project has been successfully compiled, drag and drop the newly created actor to the scene.

In addition, in order to be able to make the actor start/stop tracking (dumping the information) it is required that the `R` key is mapped to an action event `SwitchRecord` on the project input configuration.

#### Execution

Play the scene in Standalone mode, hit `R` to start recording and hit it again to stop dumping information or close the window.

#### After Executing

The tracker will generate a `.txt` file in the folder specified by the member variable `m_save_directory` in `Tracker.h`. The name of the file is specified by the corresponding variable `m_file_name`. We encourage changing those variables to a proper path and filename and then recompiling the project if the default values are not satisfactory.

That text file has the following format for each frame:

```
frame_0
timestamp frame_id
camera_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll
object_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll bbox_info
bone_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll bbox_info
[...]
frame_n
timestamp frame_id
camera_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll
object_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll bbox_info
bone_id X=x_pos Y=y_pos Z=z_pos P=pitch Y=yaw R=roll bbox_info
```

### Scene Parser

### Instance Mapper

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

#### Requirements

The following requirements must be met to execute the generator:

* Python >= 2.7
  * json
  * numpy
  * matplotlib
  * pillow
  * plyfile

### Assets

### Utils

## Known Issues and Troubleshooting

## License

Both the data and the code for The RobotriX are released under the [MIT license](LICENSE).

## Contact

Please contact Albert Garcia at [albertgg93@gmail.com](mailto:albertgg93@gmail.com) if you have any questions or requests.
